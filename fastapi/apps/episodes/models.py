from typing import List, Optional

from pydantic import BaseModel


class Episode(BaseModel):

    '''
    Episode model to represent the episode data from the API.
    Attributes:
        id (int): The id of the episode.
        name (str): The name of the episode.
        air_date (str): The air date of the episode.
        episode (str): The code of the episode.
        characters (List[str]): List of character URLs that appeared in the episode.
        url (str): Link to the episode's own URL endpoint.
        created (str): Time at which the episode was created in the database.
    '''

    id: int
    name: str
    air_date: str
    episode: str
    characters: List[str]
    url: str
    created: str
