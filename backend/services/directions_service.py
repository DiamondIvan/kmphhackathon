import os
import googlemaps
from datetime import datetime
from typing import List, Dict, Any, Optional

class DirectionsService:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("GOOGLE_MAPS_API_KEY")
        if not self.api_key:
            raise ValueError("Google Maps API key required.")
        self.client = googlemaps.Client(key=self.api_key)

    def get_directions(self, origin: str, destination: str, waypoints: Optional[List[str]] = None) -> List[Dict[str, Any]]:
        return self.client.directions(
            origin=origin,
            destination=destination,
            mode="driving",
            alternatives=True,
            departure_time=datetime.now(),
            waypoints=waypoints
        )
