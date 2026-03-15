<div align="center">

# 🧙‍♂️ LLM-DND 🐉

*An immersive, AI-powered Dungeons & Dragons adventure game utilizing advanced natural language processing and RAG to create a dynamic gaming experience.*

[![Python Version](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=flat)](https://ollama.com/)
[![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

---

**LLM-DND** is a self-hosted web application that acts as your personal Dungeon Master. By combining the power of local Large Language Models (via Ollama) with Retrieval-Augmented Generation (RAG) referencing the 5e DnD handbook, this application offers an endless, context-aware tabletop RPG experience right in your browser.

## 📑 Table of Contents

- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Architecture](#️-architecture)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Setup](#installation--setup)
- [Configuration](#️-configuration)
- [Usage](#-usage)
- [License](#-license)

---

## ✨ Features

- **Manage Models Page:** Easily configure and set up your preferred local Ollama models for both the Dungeon Master and embeddings.
- **Deep Character Creation:** Design your hero using a point-buy ability score system, and select your race, class, background, skills, and equipment (weapons/armor).
- **Play Game Page:** Engage in rich, narrative-driven adventures where the AI tracks the history and context of your entire party.
- **Adventure Storage:** Create, save, load, and delete multiple adventure histories to ensure you can pick up your campaigns right where you left off.
- **Immersive Fantasy Theme:** A beautifully styled Streamlit UI featuring the 'Cinzel' font and dark fantasy aesthetics.

---

## 🚀 Technology Stack

| Domain | Technologies |
| :--- | :--- |
| **Frontend/UI** | Python, Streamlit |
| **LLM Orchestration** | LangChain (`langchain-ollama`, `langchain-chroma`, `langchain-huggingface`) |
| **Local AI Engine** | Ollama |
| **Embeddings** | HuggingFace (`sentence-transformers`) |
| **Database (Vector & Storage)**| ChromaDB, Local Pickle/JSON files |

---

## 🏗️ Architecture

The application relies on a dual-retriever chain architecture:
1. User input is processed by a **normal retriever** (extracting rules from the 5e DnD handbook) and a **vector store retriever** (fetching historical context).
2. The context feeds into the Dungeon Master LLM to generate an immersive response.
3. The progression is saved in both chronologic lists and the history vector database.

![Chain Architecture](https://raw.githubusercontent.com/aashaybelekar/ollama-dnd-game/main/artifacts/LLM-DnD.png "Chain Architecture")

---

## 🏁 Getting Started

### Prerequisites

Ensure you have the following installed on your machine:
- **Python 3.10+** (Conda is recommended for environment management)
- **Ollama** ([Installation Guide](https://ollama.com/download))

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aashaybelekar/ollama-dnd-game.git
   cd ollama-dnd-game
   ```

2. **Start the Ollama Service:**
   Ensure Ollama is running on your machine.
   ```bash
   ollama serve
   ```
   *Verify it's running by executing `ollama -v` in a new terminal.*

3. **Pull Your Preferred Models:**
   Pull the model you want to use for the Dungeon Master (e.g., `llama3.1`).
   ```bash
   ollama pull llama3.1
   ```

4. **Set Up Python Environment:**
   Create and activate a new Conda environment:
   ```bash
   conda create -n dm_env python=3.10
   conda activate dm_env
   ```

5. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the Streamlit Application:**
   ```bash
   streamlit run main.py
   ```

---

## ⚙️ Configuration

You can configure the application by creating a `.env` file in the root directory. The application recognizes the following environment variables:

| Variable | Description | Default Value |
| :--- | :--- | :--- |
| `OLLAMA_HOST` | Hostname for your Ollama service. | `localhost` |
| `OLLAMA_PORT` | Port exposed by Ollama. | `11434` |
| `TURN_LIMIT` | Message history limit. | `10` |
| `CHROMA_DB_DIR` | Path to store the RAG vector database. | `./5e_dnd_chroma_langchain_db` |
| `HISTORY_DB_DIR`| Path to store the adventure histories. | `./history` |
| `CHARACTERS_FILE` | Path to the character JSON storage. | `characters.json` |

---

## ▶️ Usage

1. **Manage Models**: Open the app and navigate to **"Manage Models"** from the sidebar. Select your Dungeon Master Model (e.g., `llama3.1:latest`) and an Embedding Model (e.g., `sentence-transformers/all-MiniLM-L6-v2`) and click **Save Model Selections**.
2. **Create a Character**: Go to **"Play Game"** -> **"Create a Character"**. Use the character creation form to allocate ability points (max 27), set up weapons and armor, and type your backstory.
3. **Start an Adventure**: Click **"Start Adventure"**, choose your hero(es), select a difficulty (Easy, Medium, or Hard), and provide an optional custom world prompt. Let the AI DM set the scene and start your quest!

---

## 📝 License

This software is provided "AS IS", without warranty of any kind. This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
