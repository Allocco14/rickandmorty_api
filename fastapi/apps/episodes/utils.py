import requests
from apps.episodes.models import Episode
from typing import List


def get_episodes(
        page: int = 1,
    ) -> List[Episode]:
    '''
    Function to get all episodes.
    Returns:
        List[Episode]: A list of all episodes
    '''
    url = f"https://rickandmortyapi.com/api/episode/?page={page}"
    response = requests.get(url)
    data = response.json()
    if 'error' in data:
        return []
    return data['results']


def get_episode_by_id(episode_id: int) -> Episode | None:
    '''
    Function to get a episode by id.
    Args:
        episode_id (int): The id of the episode.
    Returns:
        Episode: The episode with the given id.
    '''
    url = f"https://rickandmortyapi.com/api/episode/{episode_id}"
    response = requests.get(url)
    data = response.json()
    if 'error' in data:
        return None
    return data


def get_episode_by_query(page: int, name: str, episode: str) -> List[Episode]:
    '''
    Function to get episodes by query.
    Args:
        name (str): The name of the episode.
        episode (str): The episode of the episode.
    Returns:
        List[Episode]: A list of episodes that match the query.
    '''
    url = f"https://rickandmortyapi.com/api/episode/?page={page}&"
    try:
        if name:
            url += f"name={name}&"
        if episode:
            url += f"episode={episode}"
        response = requests.get(url)
        data = response.json()
        if 'error' in data:
            return []
    except Exception as e:
        print(e)
        return []
    return data['results']
