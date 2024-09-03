import io
import json
import zipfile
from typing import List, Optional

from apps.episodes.models import Episode
from apps.episodes.utils import (get_episode_by_id, get_episode_by_query,
                                 get_episodes)
from fastapi import APIRouter
from fastapi.responses import JSONResponse, StreamingResponse

router = APIRouter()


@router.get("/get_episodes", tags=["episodes"], response_model=List[Episode])
def get_all_episodes(page: Optional[int] = 1) -> List[Episode]:
    episodes = get_episodes(page)
    return episodes


@router.get("/get_episode", tags=["episodes"], response_model=Episode | None)
def get_episode(episode_id: int) -> Episode:
    episode = get_episode_by_id(episode_id)
    return episode


@router.get("/get_episodes_query", tags=["episodes"], response_model=List[Episode])
def get_episode_query(
        name: Optional[str] = None,
        episode: Optional[str] = None,
    ) -> List[Episode]:
    episodes = get_episode_by_query(name, episode)
    if not episodes:
        return JSONResponse(content={"error": "No episodes found with the given query."}, status_code=404)
    return episodes


@router.get("/download_episodes", tags=["episodes"])
def download_episodes(
        name: Optional[str] = None,
        episode: Optional[str] = None,
    ) -> StreamingResponse:
    try:
        episodes = get_episode_by_query(name, episode)

        if not episodes:
            return JSONResponse(content={"error": "No episodes found with the given query."}, status_code=404)

        episodes_json = json.dumps(episodes, indent=4)
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            zip_file.writestr("episodes.json", episodes_json)

        zip_buffer.seek(0)
        return StreamingResponse(zip_buffer, media_type="application/zip", headers={"Content-Disposition": "attachment; filename=episodes.zip"})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
