import requests
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from langchain_ollama.llms import OllamaLLM
from langchain_core.documents import Document
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.game_workflows.loaders import load_characters
from typing import List, Generator

class OllamaApi:
    def __init__(self, model:str, temperature:int=0.7) -> None:
        try:
            self.llm = OllamaLLM(model=model, temperature=temperature)
            self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1100, chunk_overlap=100)
        except requests.RequestException as e:
            st.error(f"API call error: {str(e)}")
            return f"Error: Unable to generate content. Please check Ollama status."
    
    def start_adventure(self, characters:List[str], difficulty:str, user_prompt:str=None)->Generator:
        if not user_prompt:
            user_prompt = "make it as instreasting as possible."
        template = """
        You're a Dungeon Master for dungeons and dragons 5e.
        You'll start the adventure for the player.
        Details of players are:
            {characters_details}
        Do not describe the character.
        There are 3 possible difficulties: easy, medium and hard.
            The players have selected: {difficulty}
        Easy: You'll let their dice roll high mostly unless the demand is unreasonable
        Medium: You'll try and fail the roll where it makes sense and make the story intresting
        Hard: You can randomly choose the roll
        The player wants the world like:
            {user_prompt}
        At last give players options on what they can do, these options are not compalsory.
        You'll tell each players pov and what they are doing.
        each player will have different rolls
        """

        prompt = ChatPromptTemplate.from_template(template)

        chain = prompt | self.llm

        characters_dict = load_characters()
        characters_str = ""
        for character in characters:
            characters_str+=str(characters_dict[character])

        for chunk in chain.stream({"characters_details":characters_str, "difficulty":difficulty, "user_prompt":user_prompt}):
            yield chunk
    
    def name_adventure(self, adventure:str)->str:
        '''
        adventure(str) : it is the text when the DM sets up the start of the adventure
        '''
        template = """
        You're a Dungeon Master for dungeons and dragons 5e.
        You'll name the following DnD session.
            {adventure}
        You'll only tell the name, do not add anything else to the output other than the name.
        Don't put "" around the name
        """
        prompt = ChatPromptTemplate.from_template(template)

        chain = prompt | self.llm

        return chain.invoke({"adventure":adventure})

    def progress_story(self, chat_msg:dict[str, str], history:list)->Generator:
        def get_history(chat:dict[str, str], chat_history:list):
            history = chat_history.copy()

            history_retrieved_docs = []
            for msg in chat.values():
                history_retrieved_docs.extend(
                        st.session_state.history_store.similarity_search_by_vector_with_relevance_scores(
                        embedding=st.session_state.embedding_model.embed_query(msg), 
                        k=2,
                        filter = {
                            "uuid": st.session_state["current_uuid"]
                        }
                        )
                )

            historical_history = []
            for docs, _ in history_retrieved_docs[::-1]:
                if docs.metadata['source'] == "AI":
                    historical_history.append(AIMessage(docs.page_content))
                else:
                    historical_history.append(HumanMessage(docs.page_content))

            res_chat = [history[0][1]] # system prompt is stored for player context
            history = [hist for _, hist in history[1:]] #
            res_chat.extend(historical_history)
            res_chat.extend(history[-5:]) #last 5 messages

            return res_chat

        def get_input()->str:
            res = ""
            for character, message in chat_msg.items():
                res += f"{character} said: {message}"
                res += '\n\n'
            return res

        contextualize_q_system_prompt = (
            "Given a chat history and the latest user statement "
            "which might reference context in the chat history, "
            "formulate a standalone statement which can be understood "
            "without the chat history. Do NOT answer the statement, "
            "just reformulate it if needed and otherwise return it as is."
        )

        contextualize_q_prompt = ChatPromptTemplate.from_messages(
            [
                    ("system", contextualize_q_system_prompt),
                    MessagesPlaceholder("chat_history"),
                    ("human", "{input}"),
            ]
        )
        history_aware_retriever = create_history_aware_retriever(
            self.llm, st.session_state.vector_store, contextualize_q_prompt #generates context
        )

        system_prompt = (
            "You are a dungeon master for an adventure. "
            "Use could take help of the following pieces of retrieved context to answer. "
            "Be creative. "
            "You'll tell each players pov and what they are doing. by specifying their name."
            "each player will have different rolls"
            "\n\n"
            "{context}"
        )

        qa_prompt = ChatPromptTemplate.from_messages(
            [
                    ("system", system_prompt),
                    MessagesPlaceholder("chat_history"),
                    ("human", "{input}"),
            ]
        )


        question_answer_chain = create_stuff_documents_chain(self.llm, qa_prompt)

        rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
        
        input_text = get_input()
        history_as_message = get_history(chat=chat_msg, chat_history=history)


        for output in rag_chain.stream({"input":input_text, "chat_history":history_as_message}):
            if "answer" in output:
                yield output['answer']

    def save_doc_to_history_vector(self, doc:Document)->None:
        processed_history_docs = self.text_splitter.split_documents(documents=[doc])
        st.session_state.history_store.add_documents(documents=processed_history_docs)