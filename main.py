import streamlit as st
import os
from src.ui.theme import set_fantasy_theme
from src.utils import test_model_availability, check_ollama_availability
from src.imports.model import manage_models
from src.game_workflows.game import play_game, display_adventure_list
from src.game_workflows.player import display_character_list


from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="LLM-DND", page_icon="🧙‍♂️", layout="wide", initial_sidebar_state="expanded")
system_status = st.sidebar.empty()
ollama_placeholder = st.sidebar.empty()
model_placeholder = st.sidebar.empty()
rag_placeholder = st.sidebar.empty()

OLLAMA_HOST = os.getenv('OLLAMA_HOST', 'localhost')
OLLAMA_PORT = os.getenv("OLLAMA_PORT", "11434")
OLLAMA_API_ENDPOINT = f"http://{OLLAMA_HOST}:{OLLAMA_PORT}/api/generate"

TURN_LIMIT = int(os.getenv('TURN_LIMIT', 10))



def display_updated_status_sidebar():
    system_status.write("## System Status")
    ollama_status = "Running" if check_ollama_availability() else "Not Running"
    ollama_placeholder.write(f"Ollama Status: {ollama_status}")
    model_placeholder.write(f"Models Set: {'Yes' if 'dm_model' in st.session_state else 'No'}")
    rag_placeholder.write(f"RAG Initialized: {'Yes' if 'vector_store' in st.session_state else 'No'}")


def main():
    set_fantasy_theme()
    st.title("🧙‍♂️ LLM-DND 🐉")

    
    display_updated_status_sidebar()
    st.sidebar.divider()

    test_model_availability()

    st.session_state.page = st.sidebar.radio("Navigation", ["Play Game", "Manage Models"], index=1)

    if st.session_state.page == "Play Game":
        play_game()

        display_character_list()
        display_adventure_list()

        


    elif st.session_state.page == "Manage Models":
        manage_models()
        display_updated_status_sidebar()

    st.sidebar.divider()

    st.sidebar.info("""
    ## How to Play
    1. Go to Play Game
    2. Create your character
    3. Start New Adventure

    May your dice roll high!
    """)


if __name__ == "__main__":
    main()