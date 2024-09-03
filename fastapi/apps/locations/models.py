from pydantic import BaseModel
from typing import Optional


class Location(BaseModel):

    '''
    Location model to represent the location data from the API.

    Attributes:
        id (int): The id of the location.
        name (str): The name of the location.
        type (str): The type of the location.
        dimension (str): The dimension in which the location is located.
        residents (list): List of character URLs that live in this location.
        url (str): Link to the location's own URL endpoint.
        created (str): Time at which the location was created in the database.
    '''

    id: Optional[int] = None
    name: str
    type: Optional[str] = None
    dimension: Optional[str] = None
    residents: Optional[list] = None
    url: str
    created: Optional[str] = None
