from pydantic import BaseModel
from typing import List

class LatLng(BaseModel):
    lat: float
    lng: float

class RouteResponse(BaseModel):
    content: str = ""
    distance: str = ""
    duration: str = ""
    fuel_used: str = ""
    coordinates: List[LatLng] = []
    waypoints: List[LatLng] = []
