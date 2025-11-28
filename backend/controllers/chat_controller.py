from fastapi import APIRouter

router = APIRouter()

@router.get("/chat")
def get_chat():
    return {"message": "This is the chat endpoint"}