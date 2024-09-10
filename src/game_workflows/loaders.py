import os
import json
import pickle
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

CHARACTERS_FILE = os.getenv("CHARACTERS_FILE", "characters.json")
HISTORY_DB_DIR = os.getenv("HISTORY_DB_DIR", "./history")

def load_characters():
    if os.path.exists(CHARACTERS_FILE):
        with open(CHARACTERS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_characters(characters):
    with open(CHARACTERS_FILE, "w") as f:
        json.dump(characters, f, indent=4)

def load_adventure(uuid):
    req_path = os.path.join(HISTORY_DB_DIR, "HIST")
    hist_path = os.path.join(req_path, f"{uuid}.pkl")
    char_path = os.path.join(req_path, f"{uuid}_char.pkl")
    
    if os.path.exists(hist_path) and os.path.exists(char_path):
        with open(hist_path, "rb") as f:  # Open in binary mode for reading
            history = pickle.load(f)
        with open(char_path, "rb") as cf:
            characters = pickle.load(cf)
    else:
        raise NameError(f"History file {uuid} doesn't exist")
    return history, characters

def load_available_adventures():
    req_path = os.path.join(HISTORY_DB_DIR, "HIST", "history_ids.json")
    if os.path.exists(req_path):
        with open(req_path, "r") as f:
            return json.load(f)
    return {}

def save_adventure(uuid:str, history:list, history_names:dict, characters:list=None)->None:
    req_path = os.path.join(HISTORY_DB_DIR, "HIST")
    os.makedirs(req_path, exist_ok=True)
    
    path = os.path.join(req_path,f"{uuid}.pkl")
    with open(path, "wb") as f:
        pickle.dump(history, f)
    
    name_path = os.path.join(req_path, "history_ids.json")
    with open(name_path, "w") as f:
        json.dump(history_names, f)
    
    if characters:
        char_path = os.path.join(req_path,f"{uuid}_char.pkl")
        with open(char_path, "wb") as f:
            pickle.dump(characters, f)

def update_history_ids():
    req_path = os.path.join(HISTORY_DB_DIR, "HIST")
    name_path = os.path.join(req_path, "history_ids.json")
    with open(name_path, "w") as f:
        json.dump(st.session_state['adventure_dict'], f)


def delete_history_file(uuid):
    del st.session_state['adventure_dict'][uuid]
    path = os.path.join(HISTORY_DB_DIR, "HIST", f"{uuid}.pkl")
    char_path = os.path.join(HISTORY_DB_DIR, "HIST", f"{uuid}_char.pkl")

    history_ids = st.session_state.history_store.get(
        where={"uuid":uuid}
    )['ids']

    st.session_state.history_store.delete(history_ids)

    # Check if file exists, then delete it
    if os.path.exists(path):
        os.remove(path)
        os.remove(char_path)
        print(f"File {path} deleted successfully.")
        update_history_ids()
    else:
        print(f"File {path} not found.")
        