# MPI_project

A C# ASP.NET Core Razor Pages frontend that connects to a Python FastAPI backend serving a games database.

---

## Prerequisites

### Running manually (Windows)
Make sure the following are installed on your machine before proceeding:

- [.NET 8.0 SDK](https://dotnet.microsoft.com/download)
- [Python 3.x](https://www.python.org/downloads/)
- ⚠️ [MongoDB Community Edition](https://www.mongodb.com/try/download/community)
- [Visual Studio 2022](https://visualstudio.microsoft.com/)
- Python dependencies (from the backend folder):

```bash
pip install fastapi uvicorn pymongo python-dotenv
```

### Running with Docker (Linux)
- [Docker Engine](https://docs.docker.com/engine/install/)
- [Docker Compose plugin](https://docs.docker.com/compose/install/)

---

## Running the Project

### Option A — Manual (Windows)

#### Step 1 — Start MongoDB

Open a terminal as Administrator and run:

```bash
net start MongoDB
```

#### Step 2 — Seed the Database (first time only)

Navigate to the Python backend folder and run:

```bash
python seed.py
```

You should see `Succes!` printed in the terminal. This only needs to be done once — it populates the database with initial game data.

#### Step 3 — Start the Python Backend

In the same backend folder, run:

```bash
python -m uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`. You can verify it is running by visiting:

- `http://localhost:8000` — welcome message
- `http://localhost:8000/docs` — interactive Swagger UI

#### Step 4 — Run the C# Frontend

Open `MPIFrontend.sln` in Visual Studio 2022 and press **F5** to build and launch the application. It will open automatically in your browser.

> Make sure MongoDB and the Python backend are running **before** launching the frontend, otherwise the games list will be empty.

---

### Option B — Docker (Linux)

#### Step 1 — Install Docker

```bash
sudo apt update
sudo apt install -y ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Optionally, allow running Docker without sudo:

```bash
sudo usermod -aG docker $USER
newgrp docker
```

#### Step 2 — Start the stack

From the root of the project (where `docker-compose.yml` lives):

```bash
docker compose up --build
```

This starts all three services in the correct order: MongoDB → Backend → Frontend.

- Frontend: `http://localhost:8080`
- Backend: `http://localhost:8000`

#### Step 3 — Seed the Database (first time only)

Once all containers are running, open a second terminal and run:

```bash
docker exec mpi_backend python seed.py
```

You should see `Succes!` printed. Refresh the frontend and the games will appear.

#### Stopping the stack

```bash
docker compose down
```

---

## Troubleshooting

### Windows — Smart App Control blocking the executable

On Windows 11, Smart App Control may block the locally built executable. To fix this:

1. Search for **Smart App Control** in the Windows search bar
2. Set it to **Off**
3. Restart Visual Studio and press F5 again

---

### Linux/Docker — MongoDB requires AVX support

If MongoDB fails to start with a message about AVX support, your CPU does not support it. Use MongoDB 4.4 instead by changing the image in `docker-compose.yml`:

```yaml
mongodb:
  image: mongo:4.4
```
..and on this line, change "mongosh" to just "mongo":

```yaml
healthcheck:
    test: ["CMD", "mongo", "--eval", "db.adminCommand('ping')"]
```
---

### Linux/Docker — Containers can't reach each other

If the backend logs show `Temporary failure in name resolution`, make sure all three services have the `networks` block in `docker-compose.yml` and that the `mpi_network` bridge network is defined at the bottom. Then run:

```bash
docker compose down -v
docker network prune -f
docker compose up --build
```

---

## Project Structure

```
MPI_project/
├── .gitignore
├── README.md
├── docker-compose.yml        # Setup for MongoDB, backend and frontend containers
├── backend/
│   ├── Dockerfile            # Docker image for the Python backend
│   ├── main.py               # FastAPI app; defines all API endpoints
|   ├── pytest                # Empty test file
|   ├── requirements.txt      # Contains all necessary Python libraries in order to run the backend
│   ├── seed.py               # One-time script to populate the database with sample data
│   └── test_main.py          # Automated tests for the API
└── MPIFrontend/
    └── MPIFrontend/
        ├── Dockerfile                # Docker image for the C# frontend
        ├── Models/
        │   └── Game.cs               # C# model matching the API response
        ├── Pages/
        │   ├── Shared/
        │   │   └── _Layout.cshtml    # Shared navbar and footer layout
        │   ├── Index.cshtml          # Home page — lists all games
        │   ├── Index.cshtml.cs       # Fetches games list from GameService
        │   ├── Details.cshtml        # Game details page with Edit and Delete buttons
        │   ├── Details.cshtml.cs     # Fetches single game, handles delete
        │   ├── AddGame.cshtml        # Form to add a new game
        │   ├── AddGame.cshtml.cs     # Handles POST to create a new game
        │   ├── EditGame.cshtml       # Form to edit an existing game, pre-filled
        │   ├── EditGame.cshtml.cs    # Fetches game data, handles PUT update
        │   ├── About.cshtml          # Project info and team roles
        │   └── About.cshtml.cs
        ├── Services/
        │   └── GameService.cs        # Handles all HTTP calls to the Python API
        ├── wwwroot/
        │   ├── css/
        │   │   └── site.css          # Styling
        │   └── images/
        │       └── imdb_logo.png     # Navbar logo
        ├── appsettings.json          # Configuration including Python API base URL
        └── Program.cs                # App entry point
```

---

## API Endpoints

The Python FastAPI backend exposes the following endpoints:

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/` | Health check |
| GET | `/api/games` | Returns all games |
| GET | `/api/games/{id}` | Returns a single game by ID |
| POST | `/api/games` | Creates a new game |
| PUT | `/api/games/{id}` | Updates an existing game |
| DELETE | `/api/games/{id}` | Deletes a game |