import requests
from apps.locations.models import Location
from typing import List


def get_locations(
    page: int = 1,
) -> List[Location]:
    '''
    Function to get all locations.
    Returns:
        List[Location]: A list of all locations
    '''
    url = f"https://rickandmortyapi.com/api/location/?page={page}"
    response = requests.get(url)
    data = response.json()
    if 'error' in data:
        return []
    return data['results']


def get_location_by_id(location_id: int) -> Location | None:
    '''
    Function to get a location by id.
    Args:
        location_id (int): The id of the location.
    Returns:
        Location: The location with the given id.
    '''
    url = f"https://rickandmortyapi.com/api/location/{location_id}"
    response = requests.get(url)
    data = response.json()
    if 'error' in data:
        return None
    return data


def get_location_by_query(name: str, type: str, dimension: str) -> List[Location]:
    '''
    Function to get locations by query.
    Args:
        query (str): The query to filter the locations.
    Returns:
        List[Location]: A list of locations that match the query.
    The query can contain the following:
        - name: filter by the given name.
        - type: filter by the given type.
        - dimension: filter by the given dimension.
    '''
    url = f"https://rickandmortyapi.com/api/location/?"
    try:
        if name:
            url += f"name={name}&"
        if type:
            url += f"type={type}&"
        if dimension:
            url += f"dimension={dimension}"

        response = requests.get(url)
        data = response.json()
        if 'error' in data:
            return []
    except Exception as e:
        print(e)
        return []
    return data['results']
