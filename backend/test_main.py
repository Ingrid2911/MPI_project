from fastapi.testclient import TestClient
from main import app, collection

client = TestClient(app)

def setup_function():
    collection.delete_many({})

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Games API!"}

def test_create_valid_game():
    game_data = {
        "title": "The Witcher 3",
        "year": 2015,
        "genre": "RPG",
        "rating": 9.8,
        "description": "Un joc legendar."
    }
    response = client.post("/api/games", json=game_data)
    assert response.status_code == 201
    assert response.json()["title"] == "The Witcher 3"
    assert "id" in response.json()

def test_create_game_invalid_rating():
    game_data = {
        "title": "Cyberpunk 2077",
        "year": 2020,
        "genre": "RPG",
        "rating": 15.0, 
        "description": "Rating prea mare."
    }
    response = client.post("/api/games", json=game_data)
    assert response.status_code == 422 # Unprocessable Entity

def test_create_game_missing_title():
    game_data = {
        "year": 2022,
        "genre": "Action",
        "rating": 8.5,
        "description": "Fara titlu"
    }
    response = client.post("/api/games", json=game_data)
    assert response.status_code == 422

def test_get_all_games():
    client.post("/api/games", json={"title": "GTA V", "year": 2013, "genre": "Action", "rating": 9.5, "description": "Auto"})
    
    response = client.get("/api/games")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == "GTA V"