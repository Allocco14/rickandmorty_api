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


def get_character_by_query(page: int, name: str, status: str, species: str, type: str, gender: str) -> List[Character]:
    '''
    Function to get characters by query.
    Args:
        name (str): The name of the character.
        status (str): The status of the character.
        species (str): The species of the character.
        type (str): The type of the
        gender (str): The gender of the character.    
    Returns:
        List[Character]: A list of characters that match the query.
    
    '''
    url = f"https://rickandmortyapi.com/api/character/?page={page}&"
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
