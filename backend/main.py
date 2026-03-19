import os
import uvicorn
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from pymongo import MongoClient
from dotenv import load_dotenv
from typing import List
from bson import ObjectId

load_dotenv()

app = FastAPI(title="Games IMDb API")

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["games_db"]
collection = db["games"]

class GameModel(BaseModel):
    title: str = Field(..., min_length=1, description="Game title")
    year: int = Field(..., gt=1950, description="Release year")
    genre: str = Field(..., description="Game genre")
    rating: float = Field(..., ge=0, le=10, description="Rating from 0 to 10")
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

@app.get("/api/games/{game_id}", response_model=GameResponse)
def get_game(game_id: str):
    try:
        game = collection.find_one({"_id": ObjectId(game_id)})
    except:
        raise HTTPException(status_code=400, detail="Invalid ID format")
        
    if game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return {**game, "id": str(game["_id"])}

@app.put("/api/games/{game_id}", response_model=GameResponse)
def update_game(game_id: str, game: GameModel):
    try:
        updated_data = game.model_dump()
        result = collection.update_one({"_id": ObjectId(game_id)}, {"$set": updated_data})
    except:
        raise HTTPException(status_code=400, detail="Invalid ID format")
        
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Game not found")
        
    return {**updated_data, "id": game_id}

@app.delete("/api/games/{game_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_game(game_id: str):
    try:
        result = collection.delete_one({"_id": ObjectId(game_id)})
    except:
        raise HTTPException(status_code=400, detail="Invalid ID format")
        
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Game not found")
    return None

if __name__ == "__main__":
    print("Successfully connected to MongoDB! Starting the server...")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)