from fastapi import APIRouter

router = APIRouter()

@router.get("/route")
def get_route():
    return {"message": "This is the route endpoint"}