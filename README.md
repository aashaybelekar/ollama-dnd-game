# DnD Adventure Game

## Table of Contents
- [Technical Overview](#technical-overview)
- [Features](#features)
- [Retriever Chain Architecture](#retriever-chain-architecture)
- [App Preview](#app-preview)
- [Setup and Installation](#setup-and-installation)

## Technical Overview

This project is a Dungeons & Dragons (DnD) adventure game that utilizes advanced natural language processing and information retrieval techniques to create an immersive and dynamic gaming experience. Here are the key technical components:

- **UI Framework**: Streamlit
- **Information Retrieval**: 
  - Normal retriever for extracting information from the 5e DnD handbook
  - Vector store for storing and retrieving relevant previous history
- **Data Storage**: 
  - Vector store for efficient similarity-based retrieval
  - List-based storage for maintaining chronological history

## Features

1. **Manage Models Page**: Configure and set up the game models.
2. **Create Character Page**: Design and customize your DnD character.
3. **Play Game Page**: Engage in adventures with your created characters.
4. **Adventure Storage**: Save and load adventures for continuous gameplay.

## Retriever Chain Architecture

![Chain Architecture](https://raw.githubusercontent.com/aashaybelekar/ollama-dnd-game/main/artifacts/LLM-DnD.png "Chain Architecture")

This diagram illustrates the flow of information in our retriever chain:

1. User input is processed by both the normal retriever and the vector store retriever.
2. The normal retriever extracts relevant information from the 5e DnD handbook.
3. The vector store retriever fetches relevant previous history.
4. Both retrievers feed into the game logic.
5. The game logic generates a response, which is then used to update both the vector store and the chronological history list.

## App Preview

#### Model Selection Page
![Model page](https://raw.githubusercontent.com/aashaybelekar/ollama-dnd-game/main/artifacts/Model_setup_page.png "Model page")

#### Character Creation Page
![character page](https://raw.githubusercontent.com/aashaybelekar/ollama-dnd-game/main/artifacts/character_creation_page.png "character page")

![character page](https://raw.githubusercontent.com/aashaybelekar/ollama-dnd-game/main/artifacts/character_creation_page_2.png "character page")

![character page](https://raw.githubusercontent.com/aashaybelekar/ollama-dnd-game/main/artifacts/character_creation_page_3.png "character page")

#### Adventure Page
![Adventure page](https://raw.githubusercontent.com/aashaybelekar/ollama-dnd-game/main/artifacts/Adventure_page.png "Adventure page")

![Adventure page](https://raw.githubusercontent.com/aashaybelekar/ollama-dnd-game/main/artifacts/Chat_page.png "Adventure page")

## Setup and Installation

<div align="center">
<img alt="ollama" height="100px" src="https://github.com/ollama/ollama/assets/3325447/0d0b44e2-8f4a-4e99-9b52-a5c1c741c8f7">
</div>

### 1. Install Ollama

#### macOS

[Download](https://ollama.com/download/Ollama-darwin.zip)

#### Windows preview

[Download](https://ollama.com/download/OllamaSetup.exe)

### Linux

```
curl -fsSL https://ollama.com/install.sh | sh
```

[Manual install instructions](https://github.com/ollama/ollama/blob/main/docs/linux.md)

### 2. Run Ollama

1. On Windows and macOS: Run the application to start the ollama service
2. On linux: run the following command
    ```
    ollama serve
    ```
    To verify if it's running you can open a new terminal and run
    ```
    ollama -v
    ```
    Other details are given in the [Manual install instructions](https://github.com/ollama/ollama/blob/main/docs/linux.md) of linux

### 3. Pull the model you wish to run the game on
pull the model using
```
ollama pull {model}
```
for llama3.1:
```
ollama pull llama3.1
```

### 4. Install requirements

for best practice, make a seperate enviornment
```
conda create -n dm_env python=3.10.*
```

run the enviornment
```
conda activate dm_env
```

install the requirements
```
pip install -r requirements.txt
```

### 5. Run the streamlit application

```
streamlit run main.py
```
