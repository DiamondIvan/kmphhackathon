import os
import requests

class AIModelService:
    def __init__(self, api_key: str = None, model: str = "gemini-1.5-pro"):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.model = model
        if not self.api_key:
            raise ValueError("Gemini API key required.")

    def get_ai_response(self, user_message: str) -> str:
        if not user_message.strip():
            return "Please provide a valid message."

        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent"
            payload = {
                "prompt": [{"text": user_message}],
                "temperature": 0.7,
                "maxOutputTokens": 256
            }
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()

            candidates = data.get("candidates", [])
            if candidates and isinstance(candidates, list):
                first_candidate = candidates[0]
                content = first_candidate.get("content")
                if content:
                    return content

            return "AI did not return a response."

        except Exception as e:
            print("Error contacting AI:", str(e))
            return f"Error contacting AI: {str(e)}"
