import os
import streamlit as st
from src.game_workflows.core import start_adventure
from src.game_workflows.player import create_character_form
from src.game_workflows.loaders import load_adventure, load_available_adventures, delete_history_file

def initialize_session_state():
    if "character_creation" not in st.session_state:
        st.session_state.character_creation = False
    
    if "game_state" not in st.session_state:
        st.session_state.game_state = {"state":False}

def play_game():  
    if 'dm_model' not in st.session_state or 'vector_store' not in st.session_state or 'history_store' not in st.session_state:
        st.warning("Please set up your models in the 'Manage Models' section before playing.")
        return

    initialize_session_state()

    st.sidebar.header("Game Controls")
    if st.sidebar.button("🪄 Create a Character"):
        st.session_state['game_state']["state"] = False
        st.session_state.character_creation = True

    if st.sidebar.button("🏞️ Start Adventure"):
        reset_old_games()
        st.session_state.character_creation = False
        st.session_state['game_state']["state"] = True

    if st.session_state.character_creation:
        create_character_form()

    if st.session_state['game_state']["state"]:
        start_adventure()


def display_adventure_list():
    if "adventure_dict" not in st.session_state:
        st.session_state['adventure_dict'] = load_available_adventures()
        if not st.session_state['adventure_dict']:
            return
    
    st.sidebar.header("Created Adventures")

    for uuid, adventure_name in st.session_state['adventure_dict'].items():
        col1, col2, col3 = st.sidebar.columns([3, 1, 1])
        col1.write(adventure_name)
        if col2.button("🎮", key=f"continue_{adventure_name}"):
            initialize_adventure_state(uuid)
            start_adventure()

        if col3.button("🗑️", key=f"delete_{adventure_name}"):
            delete_history_file(uuid=uuid)
            st.sidebar.success(f"Deleted {adventure_name}")
            st.rerun()

def initialize_adventure_state(uuid):
    st.session_state["chat_history"], st.session_state["characters_in_adventure"] = load_adventure(uuid=uuid)
    st.session_state["has_adventure_started"] = True
    st.session_state["current_uuid"] = uuid
    st.rerun()

def reset_old_games():
    if "has_adventure_started" in st.session_state:
        del st.session_state["has_adventure_started"]
    if "chat_history" in st.session_state:
        del st.session_state["chat_history"]
    if "characters_in_adventure" in st.session_state:
        del st.session_state["characters_in_adventure"]