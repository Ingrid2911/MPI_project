from fastapi.testclient import TestClient
from main import app, collection

client = TestClient(app)

# Runs before each test to clean the database
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
        "description": "A legendary game."
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
        "rating": 15.0, # Rating is too high (max is 10)
        "description": "Rating is above limits."
    }
    response = client.post("/api/games", json=game_data)
    assert response.status_code == 422 # Unprocessable Entity

def test_create_game_missing_title():
    game_data = {
        "year": 2022,
        "genre": "Action",
        "rating": 8.5,
        "description": "Missing title field."
    }
    response = client.post("/api/games", json=game_data)
    assert response.status_code == 422

def test_get_all_games():
    # Insert a game first to have something to retrieve
    client.post("/api/games", json={
        "title": "GTA V", 
        "year": 2013, 
        "genre": "Action", 
        "rating": 9.5, 
        "description": "Auto theft."
    })
    
    response = client.get("/api/games")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == "GTA V"

def test_delete_game():
    create_response = client.post("/api/games", json={
        "title": "Delete Test",
        "year": 2023,
        "genre": "Test",
        "rating": 8.0,
        "description": "Delete me"
    })

    game_id = create_response.json()["id"]

    response = client.delete(f"/api/games/{game_id}")
    assert response.status_code == 204