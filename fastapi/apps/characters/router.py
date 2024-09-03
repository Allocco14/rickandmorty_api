import io
import json
from typing import List, Optional
import zipfile

from fastapi.responses import JSONResponse, StreamingResponse

from apps.characters.models import Character
from apps.characters.utils import (get_character_by_id, get_character_by_query,
                                   get_characters)
from fastapi import APIRouter

router = APIRouter()


@router.get("/get_characters", tags=["characters"], response_model=List[Character])
def get_all_characters(page: Optional[int] = 1) -> List[Character]:
    characters = get_characters(page)
    return characters


@router.get("/get_character", tags=["characters"], response_model=Character | None)
def get_character(character_id: int) -> Character:
    character = get_character_by_id(character_id)
    return character


@router.get("/get_characters_query", tags=["characters"], response_model=List[Character])
def get_character_query(
    page: Optional[int] = 1,
    name: Optional[str] = None,
    status: Optional[str] = None,
    species: Optional[str] = None,
    type: Optional[str] = None,
    gender: Optional[str] = None
) -> List[Character]:
    characters = get_character_by_query(
        page, name, status, species, type, gender)
    if not characters:
        return JSONResponse(content={"error": "No characters found with the given query."}, status_code=404)
    return characters


@router.get("/download_characters", tags=["characters"])
def download_characters(
    page: Optional[int] = 1,
    name: Optional[str] = None,
    status: Optional[str] = None,
    species: Optional[str] = None,
    type: Optional[str] = None,
    gender: Optional[str] = None
) -> StreamingResponse:
    try:
        characters = get_character_by_query(
            page, name, status, species, type, gender)

        if not characters:
            return JSONResponse(content={"error": "No characters found with the given query."}, status_code=404)

        characters_json = json.dumps(characters, indent=4)
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            zip_file.writestr("characters.json", characters_json)

        zip_buffer.seek(0)
        return StreamingResponse(
            zip_buffer, media_type="application/zip", headers={"Content-Disposition": "attachment; filename=characters.zip"})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
