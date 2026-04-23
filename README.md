# MPI_project

A C# ASP.NET Core Razor Pages frontend that connects to a Python FastAPI backend serving a games database.

---

## Prerequisites

Make sure the following are installed on your machine before proceeding:

- [.NET 8.0 SDK](https://dotnet.microsoft.com/download)
- [Python 3.x](https://www.python.org/downloads/)
- ⚠️ [MongoDB Community Edition](https://www.mongodb.com/try/download/community)
- [Visual Studio 2022](https://visualstudio.microsoft.com/)
- Python dependencies (from the backend folder):

```bash
pip install fastapi uvicorn pymongo python-dotenv
```

---

## Running the Project

### Step 1 — Start MongoDB

Open a terminal as Administrator and run:

```bash
net start MongoDB
```

---

### Step 2 — Seed the Database (first time only)

Navigate to the Python backend folder and run:

```bash
python seed.py
```

You should see `Succes!` printed in the terminal. This only needs to be done once — it populates the database with initial game data.

---

### Step 3 — Start the Python Backend

In the same backend folder, run:

```bash
python -m uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`. You can verify it is running by visiting:

- `http://localhost:8000` — welcome message
- `http://localhost:8000/docs` — interactive Swagger UI

---

### Step 4 — Run the C# Frontend

Open `MPIFrontend.sln` in Visual Studio 2022 and press **F5** to build and launch the application. It will open automatically in your browser.

> Make sure MongoDB and the Python backend are running **before** launching the frontend, otherwise the games list will be empty.

---

## Troubleshooting

### Windows Smart App Control blocking the executable

On Windows 11, Smart App Control may block the locally built executable with a message like:

> *"An Application Control policy has blocked this file"*

or

> *"Part of this app has been blocked"*

**To fix this:**

1. Open the Windows search bar and search for **Smart App Control**
2. Click on **Smart App Control settings**
3. Set Smart App Control to **Off**
4. Restart Visual Studio and press F5 again

> This is safe to do on a personal development machine. Smart App Control is enabled by default on fresh Windows 11 installs and commonly blocks locally built executables that are not code-signed.

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

## TODO: Add support for running with Docker (needs Linux)