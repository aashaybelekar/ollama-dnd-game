import os
import requests
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

OLLAMA_HOST = os.getenv('OLLAMA_HOST', 'localhost')
OLLAMA_PORT = os.getenv("OLLAMA_PORT", "11434")
OLLAMA_API_ENDPOINT = f"http://{OLLAMA_HOST}:{OLLAMA_PORT}/api/generate"

def check_ollama_availability():
    try:
        response = requests.get(OLLAMA_API_ENDPOINT.replace('/api/generate', '/api/version'), timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def test_model_availability():
    if not check_ollama_availability():
        st.error("Ollama is not available. Please make sure it's running and configured correctly.")
        st.info("To start Ollama, open a terminal and run the 'ollama serve' command.")
        if st.button("Retry Connection"):
            st.experimental_rerun()
    return