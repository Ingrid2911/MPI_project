import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

games_to_insert = [
    {
        "title": "The Witcher 3: Wild Hunt",
        "year": 2015,
        "genre": "RPG",
        "rating": 9.8,
        "description": "As Geralt of Rivia, explore a massive open world to find the child of prophecy."
    },
    {
        "title": "Red Dead Redemption 2",
        "year": 2018,
        "genre": "Action-Adventure",
        "rating": 9.7,
        "description": "An epic tale of life in America's unforgiving heartland."
    },
    {
        "title": "Minecraft",
        "year": 2011,
        "genre": "Sandbox",
        "rating": 9.0,
        "description": "Explore infinite worlds and build everything from the simplest of homes to the grandest of castles."
    },
    {
        "title": "Portal 2",
        "year": 2011,
        "genre": "Puzzle-Platformer",
        "rating": 9.5,
        "description": "A mind-bending puzzle game using physics and portals."
    },
    {
        "title": "God of War",
        "year": 2018,
        "genre": "Action",
        "rating": 9.6,
        "description": "Kratos must adapt to unfamiliar lands, unexpected threats, and a second chance at being a father."
    }
]

try:
    client = MongoClient(MONGO_URI)
    db = client["games_db"]
    collection = db["games"]
    
    collection.delete_many({})
    
    collection.insert_many(games_to_insert)
    print("Succes!")
except Exception as e:
    print(f"Error: {e}")