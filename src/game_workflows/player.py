import os
import json
from requests import session
import streamlit as st
from typing import Dict, Tuple
from src.game_workflows.loaders import save_characters, load_characters
from src.game_workflows.references import weapon_dict, armor_dict
from dotenv import load_dotenv
load_dotenv()

TOTAL_SKILL_POINTS = int(os.getenv('TOTAL_MAX_POINTS_AT_START', 27))


def create_character_form():
    def initialize_session_state():
        if 'character_created' not in st.session_state:
            st.session_state.character_created = False
        if 'ability_scores' not in st.session_state:
            st.session_state.ability_scores = {ability: 8 for ability in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]}
        if 'remaining_points' not in st.session_state:
            st.session_state.remaining_points = TOTAL_SKILL_POINTS

    def calculate_points_spent(score):
        # Point buy system calculation
        return score - 8

    def update_ability_score(ability):
        old_score = st.session_state.ability_scores[ability]
        new_score = st.session_state[f"ability_{ability}"]
        
        old_points = calculate_points_spent(old_score)
        new_points = calculate_points_spent(new_score)
        
        st.session_state.ability_scores[ability] = new_score
        st.session_state.remaining_points += old_points - new_points
    
    def reset_character_form():
        st.session_state.ability_scores = {ability: 8 for ability in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]}
        st.session_state.remaining_points = TOTAL_SKILL_POINTS
    
    initialize_session_state()

    st.header("Character Creation Form")
    st.divider()

    # Basic Information
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Character Name", key="character_name")
        race = st.selectbox("Race", ["Human", "Elf", "Dwarf", "Halfling", "Gnome", "Half-Orc", "Tiefling"], key="race")
    with col2:
        character_class = st.selectbox("Class", ["Fighter", "Wizard", "Rogue", "Cleric", "Paladin", "Ranger", "Barbarian"], key="class")
        background = st.selectbox("Background", ["Acolyte", "Criminal", "Folk Hero", "Noble", "Sage", "Soldier"], key="background")

    # Ability Scores with Point Buy
    st.divider()
    st.subheader("Ability Scores")
    st.write(f"Total points remaining: {st.session_state.remaining_points}")

    abilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    col1, col2 = st.columns(2)
    
    for i, ability in enumerate(abilities):
        with col1 if i % 2 == 0 else col2:
            score = st.number_input(
                f"{ability}", 
                min_value=8, 
                max_value=15, 
                value=st.session_state.ability_scores[ability], 
                key=f"ability_{ability}",
                on_change=update_ability_score,
                args=(ability,)
            )
            
            # Update session state
            old_score = st.session_state.ability_scores[ability]
            st.session_state.ability_scores[ability] = score
            
            # Recalculate points
            old_points = calculate_points_spent(old_score)
            new_points = calculate_points_spent(score)
            st.session_state.remaining_points += old_points - new_points
            
            st.write(f"Points spent: {new_points}")


    if st.session_state.remaining_points < 0:
        st.warning("You have exceeded the available points!")
    elif st.session_state.remaining_points > 0:
        st.warning("You still have points to allocate!")

    # Skills
    st.divider()
    st.subheader("Skills")
    skills = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", 
              "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", 
              "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]
    
    selected_skills = st.multiselect("Select Skills (based on your class)", skills, key="skills")

    # Equipment
    st.divider()
    st.subheader("Equipment")
    
    col1, col2 = st.columns(2)
    with col1:
        weapon_type = st.radio("Weapon Type", weapon_dict.keys(), key="weapon_type")
        selected_weapon_name = st.radio("Armor", weapon_dict[weapon_type], key="weapon")
        weapon_details = weapon_dict[weapon_type][selected_weapon_name]

    with col2:
        st.write("Weapon Details:")
        for key, value in weapon_details.items():
            if key == "Cost":
                continue
            st.write(f"{key}: {value}")

    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        armor_type = st.radio("Armor Type", armor_dict.keys(), key="armor_type")
    
        selected_armor_name = st.radio("Armor", armor_dict[armor_type],key="armor")
        # Get the selected armor details
        armor_details = armor_dict[armor_type][selected_armor_name]
    
    with col2:
        # Display armor details
        st.write("Armor Details:")
        for key, value in armor_details.items():
            if key == "Cost":
                continue
            st.write(f"{key}: {value}")


    other_equipment = st.text_area("Other Equipment", key="other_equipment")

    # Character Description
    st.divider()
    st.subheader("Character Description")
    appearance = st.text_area("Appearance", key="appearance")
    personality = st.text_area("Personality Traits", key="personality")
    bonds = st.text_input("Bonds", key="bonds")
    flaws = st.text_input("Flaws", key="flaws")

    # Backstory
    st.divider()
    st.subheader("Backstory")
    backstory = st.text_area("Character Backstory", key="backstory")

    if st.button("Save Character"):
        if name and name not in st.session_state.characters:
            character_data = {
                "name": name,
                "race": race,
                "class": character_class,
                "background": background,
                "ability_scores": st.session_state.ability_scores.copy(),
                "skills": selected_skills,
                "weapons": selected_weapon_name,
                "armor": selected_armor_name,
                "other_equipment": other_equipment,
                "appearance": appearance,
                "personality": personality,
                "bonds": bonds,
                "flaws": flaws,
                "backstory": backstory
            }
            st.session_state.characters[name] = character_data
            save_characters(st.session_state.characters)
            st.success(f"Character '{name}' saved successfully!")
            reset_character_form()
            st.success("Character saved successfully!")
            st.rerun()
        elif not name:
            st.error("Please enter a character name before saving.")
        else:
            st.error(f"A character named '{name}' already exists. Please choose a different name.")

def display_character_list():
    if "character" not in st.session_state:
        st.session_state.characters = load_characters()
        if not st.session_state.characters:
            return
    st.sidebar.header("Created Characters")
    for char_name in st.session_state.characters:
        col1, col2 = st.sidebar.columns([3, 1])
        col1.write(char_name)
        if col2.button("🗑️", key=f"delete_{char_name}"):
            del st.session_state.characters[char_name]
            st.sidebar.success(f"Deleted {char_name}")
            save_characters(st.session_state.characters)
            st.rerun()