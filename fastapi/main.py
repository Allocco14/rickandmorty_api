from fastapi import FastAPI

app = FastAPI()
app.title = "Rick & Morty API Consumer"
app.version = "0.0.1"

@app.get("/")
def home():
    return {"message": "Hello World"}

API_URL = "https://rickandmortyapi.com/api/character"


@app.get("/get_characters")
def get_characters():
    
    import requests
    import json

    response = requests.get(API_URL)
    data = response.json()
    return data
