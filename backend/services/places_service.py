import os
from googlemaps import Client as GoogleMaps
from typing import List

class PlacesService:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("GOOGLE_MAPS_API_KEY")
        if not self.api_key:
            raise ValueError("Google Maps API key required.")
        self.client = GoogleMaps(key=self.api_key)

    def get_autocomplete(self, input_text: str) -> List[str]:
        try:
            predictions = self.client.places_autocomplete(input_text)
            return [p["description"] for p in predictions][:4]
        except Exception as e:
            print("Error fetching autocomplete:", str(e))
            return []
