# Games IMDB

> A computer games rating platform designed to help users discover, evaluate, and rank video games through a centralized full-stack application.

---

# 1. Description and Objectives

Games IMDB is a full-stack web platform that allows users to browse, rate, add, edit, and manage computer games within a structured database environment.

### Problem Solved:

* Hierarchization and ranking of computer games
* Centralized management of game information
* Accessible platform for evaluating and organizing games

### Objectives:

* Provide a reliable games database
* Allow CRUD operations for game management
* Support user-friendly game discovery and comparison
* Ensure stable backend/frontend integration

### Target Audience:

* Gamers
* Children
* Teenagers

---

# 2. Team and Roles

| Student Name    | Main Role          | GitHub Username  |
| --------------- | ------------------ | ---------------- |
| Negru Cosmin    | Backend Developer  | @cnegru38        |
| Răuțoiu Marco   | DevOps Engineer    | @RautoiuMarco    |
| Mihăiță Ingrid  | QA Engineer        | @Ingrid2911      |
| Popîrdă Eusebiu | Frontend Developer | @popardasebi3490 |

---

# 3. Architecture and Technologies

* **Backend:** Python FastAPI
* **Frontend:** C# ASP.NET Core Razor Pages
* **Database:** MongoDB
* **DevOps:** Docker & Docker Compose
* **Testing:** Pytest + FastAPI TestClient

---

# 4. Local Setup (How to Run the Project)

## Prerequisites

### Running manually (Windows)

Make sure the following are installed on your machine before proceeding:

* [.NET 8.0 SDK](https://dotnet.microsoft.com/download)
* [Python 3.x](https://www.python.org/downloads/)
* [MongoDB Community Edition](https://www.mongodb.com/try/download/community)
* [Visual Studio 2022](https://visualstudio.microsoft.com/)
* Python dependencies (from the backend folder):

```bash id="9qqvv8"
pip install fastapi uvicorn pymongo python-dotenv
```

### Running with Docker (Linux)

* Docker Engine
* Docker Compose plugin

---

## Running the Project

### Option A — Manual (Windows)

#### Step 1 — Start MongoDB

```bash id="ytvr5d"
net start MongoDB
```

#### Step 2 — Seed the Database (first time only)

```bash id="pz3w9g"
python seed.py
```

#### Step 3 — Start the Python Backend

```bash id="lwm2b4"
python -m uvicorn main:app --reload
```

### API Verification:

* `http://localhost:8000`
* `http://localhost:8000/docs`

#### Step 4 — Run the C# Frontend

Open `MPIFrontend.sln` in Visual Studio 2022 and press:

```bash id="ckcr6c"
F5
```

---

### Option B — Docker (Linux)

#### Step 1 — Install Docker

Follow Docker official installation instructions.

#### Step 2 — Start the full stack

```bash id="j3t3pr"
docker compose up --build
```

### Services:

* Frontend: `http://localhost:8080`
* Backend: `http://localhost:8000`

#### Step 3 — Seed the Database

```bash id="t4gc1r"
docker exec mpi_backend python seed.py
```

#### Stop services:

```bash id="j8u38y"
docker compose down
```

---

# 5. Troubleshooting

### Windows

If Smart App Control blocks the executable:

* Disable Smart App Control
* Restart Visual Studio

---

### Linux/Docker

### MongoDB AVX issue:

Use:

```yaml id="2n59rn"
image: mongo:4.4
```

### Network resolution issues:

```bash id="ijwx04"
docker compose down -v
docker network prune -f
docker compose up --build
```

---

# 6. Project Structure

```plaintext id="eb5i6t"
MPI_project/
├── .gitignore
├── README.md
├── docker-compose.yml
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   ├── pytest
│   ├── requirements.txt
│   ├── seed.py
│   └── test_main.py
└── MPIFrontend/
    └── MPIFrontend/
        ├── Dockerfile
        ├── Models/
        ├── Pages/
        ├── Services/
        ├── wwwroot/
        ├── appsettings.json
        └── Program.cs
```

---

# 7. API Endpoints

| Method | URL               | Description                 |
| ------ | ----------------- | --------------------------- |
| GET    | `/`               | Health check                |
| GET    | `/api/games`      | Returns all games           |
| GET    | `/api/games/{id}` | Returns a single game by ID |
| POST   | `/api/games`      | Creates a new game          |
| PUT    | `/api/games/{id}` | Updates an existing game    |
| DELETE | `/api/games/{id}` | Deletes a game              |

---

