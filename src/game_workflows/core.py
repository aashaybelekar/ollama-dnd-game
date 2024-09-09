import os
import streamlit as st
from uuid import uuid4
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.documents import Document
from src.game_workflows.player import load_characters
from src.game_workflows.loaders import save_adventure
from dotenv import load_dotenv
load_dotenv()

TURN_LIMIT = int(os.getenv('TURN_LIMIT', 10))
def initialise_adventure_session_state():
    if "has_adventure_started" not in st.session_state:
        st.session_state["has_adventure_started"] = False
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"]:list(AIMessage|HumanMessage|SystemMessage) = []
    if "adventure_dict" not in st.session_state:
        st.session_state['adventure_dict'] = {}
    if "characters_in_adventure" not in st.session_state:
        st.session_state["characters_in_adventure"] = []

def start_adventure():
    initialise_adventure_session_state()
    has_adventure_started = st.session_state["has_adventure_started"]

    st.header("📜 Adventure Log")
    st.divider()
    characters = load_characters()
    adventure_user_prompt = None
    characters_in_adventure = None
    if not has_adventure_started:
        st.session_state["characters_in_adventure"] = st.multiselect("Which hero will you choose for this adventure?", characters.keys())

        adventure_difficulty = st.radio("Select Difficulty", ["Easy", "Medium", "Hard"], key="adventure_difficulty")

        if st.button("Set Adventure Prompt"):
            adventure_user_prompt = st.text_area("Adventure Prompt", key="appearance")
            if adventure_user_prompt:
                st.success("Adventure world changed to your accord.")

        if st.session_state["characters_in_adventure"]:
            if st.button("Start Adventure"):
                with st.spinner("Creating World.."):
                    adventure_start = st.write_stream(st.session_state["api"].start_adventure(st.session_state["characters_in_adventure"], adventure_difficulty, adventure_user_prompt))
                
                st.session_state["has_adventure_started"] = True

                with st.spinner("Thinking of a name for this adventure.."):
                    adventure_name = st.session_state['api'].name_adventure(adventure_start)
                
                st.session_state["current_uuid"] = str(uuid4())

                st.session_state['adventure_dict'][st.session_state["current_uuid"]] = adventure_name
                st.session_state["chat_history"].append((None, SystemMessage(adventure_start)))

                history_document = Document(page_content=adventure_start, metadata={'source':"AI", "uuid":st.session_state["current_uuid"]})

                st.session_state['api'].save_doc_to_history_vector(history_document)

                with st.spinner("Saving.."):
                    save_adventure(st.session_state["current_uuid"], history=st.session_state["chat_history"], history_names=st.session_state['adventure_dict'])
                st.rerun()
    
        if not st.session_state["characters_in_adventure"]:
            st.info("The adventure needs to had at least 1 hero.")

    if st.session_state["chat_history"]:
        history_container = st.container()
        with history_container:
            for character, message in st.session_state["chat_history"]:
                if character:  # Character's messages
                    st.markdown(f"**🗣️ {character}:** {message.content}")
                else:  # System messages or narration
                    st.markdown(f"**Narrator:** {message.content}")
    
    if has_adventure_started:
        st.subheader("🗨️ Adventure Chat")

        # Create a chat-like box
        st.container()

        # Message Input Area
        with st.form(key='chat_form', clear_on_submit=True):
            speaking_character = st.selectbox(
                "Which character is talking?", 
                st.session_state.characters_in_adventure
            )
            chat_message = st.text_area("Enter message", height=100)
            submit_button = st.form_submit_button("➡️")

        # Handle form submission
        if submit_button and chat_message:
            # Store the new message in chat history
            st.session_state["chat_history"].append((speaking_character, HumanMessage(chat_message)))
            history_document = Document(page_content=chat_message, metadata={'source':f"{speaking_character}", "uuid":st.session_state["current_uuid"]})

            st.session_state['api'].save_doc_to_history_vector(history_document)

            with st.spinner("Thinking.."):
                adventure_progression = st.write_stream(st.session_state["api"].progress_story(speaking_character, chat_message, st.session_state["chat_history"]))
            
            st.session_state['chat_history'].append((None, AIMessage(adventure_progression)))
            history_document = Document(page_content=adventure_progression, metadata={'source':"AI", "uuid":st.session_state["current_uuid"]})

            st.session_state['api'].save_doc_to_history_vector(history_document)

            st.rerun()

