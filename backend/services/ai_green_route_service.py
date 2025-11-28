from typing import Dict, Any

class AIGreenRouteService:
    def find_best_route(self, directions_result: Dict[str, Any]) -> Dict[str, Any]:
        if not directions_result or "routes" not in directions_result or len(directions_result["routes"]) == 0:
            return directions_result

        best_route = min(
            directions_result["routes"],
            key=lambda r: r["legs"][0]["distance"]["value"]
        )

        return {
            "routes": [best_route],
            "geocoded_waypoints": directions_result.get("geocoded_waypoints", [])
        }
