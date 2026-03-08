import os
from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI(title="Games IMDb API")

# Database connection setup
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

try:
    client = MongoClient(MONGO_URI)
    db = client["games_db"]
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(f"MongoDB connection error: {e}")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Games API!"}

@app.get("/api/status")
def check_status():
    return {"status": "API and Database are running perfectly!"}