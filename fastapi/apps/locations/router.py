import io
import json
import zipfile
from typing import List, Optional

from apps.locations.models import Location
from apps.locations.utils import (get_location_by_id, get_location_by_query,
                                 get_locations)
from fastapi import APIRouter
from fastapi.responses import JSONResponse, StreamingResponse

router = APIRouter()


@router.get("/get_locations", tags=["locations"], response_model=List[Location])
def get_all_locations(page: Optional[int] = 1) -> List[Location]:
    locations = get_locations(page)
    return locations


@router.get("/get_location", tags=["locations"], response_model=Location | None)
def get_location(location_id: int) -> Location:
    location = get_location_by_id(location_id)
    return location


@router.get("/get_locations_query", tags=["locations"], response_model=List[Location])
def get_location_query(
        name: Optional[str] = None,
        type: Optional[str] = None,
        dimension: Optional[str] = None
    ) -> List[Location]:
    locations = get_location_by_query(name, type, dimension)
    if not locations:
        return JSONResponse(content={"error": "No locations found with the given query."}, status_code=404)
    return locations


@router.get("/download_locations", tags=["locations"])
def download_locations(
        name: Optional[str] = None,
        type: Optional[str] = None,
        dimension: Optional[str] = None
    ) -> StreamingResponse:
    try:
        locations = get_location_by_query(name, type, dimension)

        if not locations:
            return JSONResponse(content={"error": "No locations found with the given query."}, status_code=404)

        locations_json = json.dumps(locations, indent=4)
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            zip_file.writestr("locations.json", locations_json)

        zip_buffer.seek(0)
        return StreamingResponse(
            zip_buffer, media_type="application/zip", headers={"Content-Disposition": "attachment; filename=locations.zip"})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
