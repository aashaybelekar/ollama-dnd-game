from typing import Dict, Tuple
from src.api_workflows.call_api import api_call

def start_new_adventure(model: str, party_members: Dict[str, str]) -> Tuple[Dict, str]:
    dm_intro = api_call(model,
                        f"You are the Dungeon Master. Start an exciting and unique D&D adventure. Introduce the characters: {', '.join(party_members.keys())}. Set the scene and present an initial challenge or mystery.",
                        300)
    return {
        "turn": 1,
        "story_progression": [dm_intro],
        "turn_participation": {name: False for name in party_members},
        "party_members": party_members
    }, dm_intro

def dm_turn(model: str, game_state: Dict, vector_store) -> str:
    context = vector_store.similarity_search(" ".join(game_state['story_progression'][-5:]), k=3)
    dm_prompt = f"As the Dungeon Master, consider the recent events:\n{' '.join(game_state['story_progression'][-5:])}\nRelevant lore: {' '.join([doc.page_content for doc in context])}\nSummarize the actions, introduce the next challenge or plot development, and describe the scene. Be creative and engaging."
    return api_call(model, dm_prompt, 300)