import os
import requests
import streamlit as st
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from src.api_workflows.call_api import OllamaApi
from dotenv import load_dotenv


load_dotenv()
OLLAMA_HOST = os.getenv('OLLAMA_HOST', 'localhost')
OLLAMA_PORT = os.getenv("OLLAMA_PORT", "11434")
OLLAMA_API_ENDPOINT = f"http://{OLLAMA_HOST}:{OLLAMA_PORT}/api/generate"

CHROMA_DB_DIR = os.getenv('CHROMA_DB_DIR', './5e_dnd_chroma_langchain_db')
HISTORY_DB_DIR = os.getenv('HISTORY_DB_DIR', "./history")

@st.cache_resource
def initialize_rag():
    handbook_store = Chroma(embedding_function=st.session_state.embedding_model, persist_directory=CHROMA_DB_DIR)
    return handbook_store.as_retriever()

@st.cache_resource
def initialize_history():
    history_store = Chroma(embedding_function=st.session_state.embedding_model, persist_directory=HISTORY_DB_DIR)
    return history_store

def manage_models():
    def list_ollama_models():
        try:
            response = requests.get(OLLAMA_API_ENDPOINT.replace('/api/generate', '/api/tags'))
            if response.status_code == 200:
                return [model['name'] for model in response.json().get('models', [])]
            return []
        except requests.RequestException:
            return []
        
    st.header("Manage Models")

    models = list_ollama_models()
    if not models:
        st.warning("No Ollama models found or Ollama is not running.")
        return

    st.subheader("Available Ollama Models")
    for model in models:
        st.write(f"- {model}")

    st.subheader("Select Models")
    dm_model = st.selectbox("Dungeon Master Model", models,
                            index=models.index(st.session_state.get('dm_model', models[0])))
    embedding_model = st.selectbox("RAG Embedding Model", ["sentence-transformers/all-MiniLM-L6-v2",
                                                           "sentence-transformers/all-mpnet-base-v2"])

    if st.button("Save Model Selections"):
        st.session_state.dm_model = dm_model
        st.session_state.api:OllamaApi = OllamaApi(model=dm_model) # type: ignore
        st.session_state.embedding_model = HuggingFaceEmbeddings(model_name=embedding_model)
        st.session_state.vector_store = initialize_rag() # retriver
        st.session_state.history_store = initialize_history() # non retriver
        st.success("Model selections saved!")



