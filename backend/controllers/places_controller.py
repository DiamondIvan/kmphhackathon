from fastapi import APIRouter

router = APIRouter()

@router.get("/places")
def get_places():
    return {"message": "This is the places endpoint"}