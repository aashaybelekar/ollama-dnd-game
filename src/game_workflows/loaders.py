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
        json.dump(characters, f)

def load_adventure(uuid:str)->list:
    req_path = os.path.join(HISTORY_DB_DIR, "HIST", f"{uuid}.pkl")
    if os.path.exists(req_path):
        with open(req_path, "rb") as f:  # Open in binary mode for reading
            history = pickle.load(f)
    else:
        raise NameError(f"History file {uuid} doesn't exist")
    return history

def load_available_adventures():
    req_path = os.path.join(HISTORY_DB_DIR, "HIST", "history_ids.json")
    if os.path.exists(req_path):
        with open(req_path, "r") as f:
            return json.load(f)
    return {}

def save_adventure(uuid:str, history:list, history_names:dict)->None:
    req_path = os.path.join(HISTORY_DB_DIR, "HIST")
    os.makedirs(req_path, exist_ok=True)
    if history:
        path = os.path.join(req_path,f"{uuid}.pkl")
        with open(path, "wb") as f:
            pickle.dump(history, f)
    else:
        print("Only history names were updated")
    
    name_path = os.path.join(req_path, "history_ids.json")
    with open(name_path, "w") as f:
        json.dump(history_names, f)

def update_history_ids():
    req_path = os.path.join(HISTORY_DB_DIR, "HIST")
    name_path = os.path.join(req_path, "history_ids.json")
    with open(name_path, "w") as f:
        json.dump(st.session_state['adventure_dict'], f)


def delete_history_file(uuid):
    del st.session_state['adventure_dict'][uuid]
    path = os.path.join(HISTORY_DB_DIR, "HIST", f"{uuid}.pkl")
    
    # Check if file exists, then delete it
    if os.path.exists(path):
        os.remove(path)
        print(f"File {path} deleted successfully.")
        update_history_ids()
    else:
        print(f"File {path} not found.")
        