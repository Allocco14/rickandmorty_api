import requests
from apps.characters.models import Character
from typing import List


def get_characters(
    page: int = 1,
) -> List[Character]:
    '''
    Function to get all characters.
    Returns:
        List[Character]: A list of all characters
    '''
    url = f"https://rickandmortyapi.com/api/character/?page={page}"
    response = requests.get(url)
    data = response.json()
    if 'error' in data:
        return []
    return data['results']


def get_character_by_id(character_id: int) -> Character | None:
    '''
    Function to get a character by id.
    Args:
        character_id (int): The id of the character.
    Returns:
        Character: The character with the given id.
    '''
    url = f"https://rickandmortyapi.com/api/character/{character_id}"
    response = requests.get(url)
    data = response.json()
    if 'error' in data:
        return None
    return data


def get_character_by_query(name: str, status: str, species: str, type: str, gender: str) -> List[Character]:
    '''
    Function to get characters by query.
    Args:
        query (str): The query to filter the characters.
    Returns:
        List[Character]: A list of characters that match the query.
    The query can contain the following:
        - name: filter by the given name.
        - status: filter by the given status (alive, dead or unknown).
        - species: filter by the given species.
        - type: filter by the given type.
        - gender: filter by the given gender (female, male, genderless or unknown).
    '''
    url = f"https://rickandmortyapi.com/api/character/?"
    try:
        if name:
            url += f"name={name}&"
        if status:
            url += f"status={status}&"
        if species:
            url += f"species={species}&"
        if type:
            url += f"type={type}&"
        if gender:
            url += f"gender={gender}"
        response = requests.get(url)
        data = response.json()
        if 'error' in data:
            return []
    except Exception as e:
        print(e)
        return []
    return data['results']
