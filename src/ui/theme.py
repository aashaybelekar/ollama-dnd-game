import streamlit as st

def set_fantasy_theme():
    st.markdown("""
    <style>
        body { color: #e0e0e0; background-color: #1a1a2e; font-family: 'Cinzel', serif; }
        .stButton>button { color: #ffd700; background-color: #4a0e0e; border: 2px solid #ffd700; }
        .stTextInput>div>div>input, .stTextArea>div>div>textarea { color: #e0e0e0; background-color: #2a2a4e; }
        .stHeader { color: #ffd700; text-shadow: 2px 2px 4px #000000; }
        .sidebar .sidebar-content { background-color: #16213e; }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)