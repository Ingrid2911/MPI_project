import os
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from pymongo import MongoClient
from dotenv import load_dotenv
from typing import List

load_dotenv()

app = FastAPI(title="Games IMDb API")

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["games_db"]
collection = db["games"]

class GameModel(BaseModel):
    title: str = Field(..., min_length=1, description="Titlul jocului")
    year: int = Field(..., gt=1950, description="Anul lansarii")
    genre: str = Field(..., description="Genul jocului")
    rating: float = Field(..., ge=0, le=10, description="Nota de la 0 la 10")
    description: str

class GameResponse(GameModel):
    id: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Games API!"}

@app.post("/api/games", response_model=GameResponse, status_code=status.HTTP_201_CREATED)
def create_game(game: GameModel):
    game_dict = game.model_dump()
    result = collection.insert_one(game_dict)

    created_game = {**game_dict, "id": str(result.inserted_id)}
    return created_game

@app.get("/api/games", response_model=List[GameResponse])
def get_games():
    games = []
    for game in collection.find():
        game_data = {**game, "id": str(game["_id"])}
        games.append(game_data)
    return games