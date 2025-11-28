from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.chat_controller import router as chat_router
from controllers.route_controller import router as route_router
from controllers.places_controller import router as places_router

app = FastAPI()

# CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat_router)
app.include_router(route_router)
app.include_router(places_router)

@app.get("/")
def root():
    return {"message": "FastAPI backend running"}
