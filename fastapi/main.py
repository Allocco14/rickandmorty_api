from fastapi import FastAPI
from apps.characters.router import router as characters_router
from apps.episodes.router import router as episodes_router
from apps.locations.router import router as locations_router

BASE_URL = "https://rickandmortyapi.com/api/character"

app = FastAPI()
app.title = "Rick & Morty API Consumer"
app.version = "0.0.1"

app.include_router(characters_router, prefix="/api/v1")
app.include_router(episodes_router, prefix="/api/v1")
app.include_router(locations_router, prefix="/api/v1")
