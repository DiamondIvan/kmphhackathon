from ai_green_route_service import AIGreenRouteService
from typing import Dict, Any

class GreenRouteService:
    def __init__(self, ai_green_route_service: AIGreenRouteService = None):
        self.ai_green_route_service = ai_green_route_service or AIGreenRouteService()

    def get_green_route(self, directions_result: Dict[str, Any]) -> Dict[str, Any]:
        return self.ai_green_route_service.find_best_route(directions_result)
