from typing import List

from pydantic import BaseModel

from apps.locations.models import Location


class Character(BaseModel):
    '''
    Character model to represent the character data from the API.
    
    Attributes:
        id (int): The id of the character.
        name (str): The name of the character.
        status (str): The status of the character ('Alive', 'Dead' or 'unknown').
        species (str): The species of the character.
        type (str): The type or subspecies of the character.
        gender (str): The gender of the character ('Female', 'Male', 'Genderless' or 'unknown').
        origin (Location): Name and link to the character's origin location.
        location (Location): Name and link to the character's last known location endpoint.
        image (str): Link to the character's image.
        episode (List[str]): List of episodes in which this character appeared.
        url (str): Link to the character's own URL endpoint.
        created (str): Time at which the character was created in the database.
    '''

    id: int
    name: str
    status: str
    species: str
    type: str
    gender: str
    origin: dict
    location: dict
    image: str
    episode: List[str]
    url: str
    created: str
