# Games IMDB

> Platformă de rating al jocurilor pe calculator, destinată evaluării, descoperirii și ierarhizării celor mai populare titluri pentru gameri.

---

# 1. Descriere și Obiective

Games IMDB este o aplicație full-stack care permite utilizatorilor să vizualizeze, adauge, editeze și gestioneze jocuri video într-o bază de date centralizată.

### Problema rezolvată:

* Ierarhizarea jocurilor pe calculator
* Organizarea informațiilor despre jocuri într-un sistem accesibil
* Oferirea unei platforme pentru evaluare și administrare

### Public țintă:

* Gameri
* Copii
* Adolescenți

---

# 2. Echipa și Roluri

| Nume Student    | Rol Principal      | GitHub Username  |
| --------------- | ------------------ | ---------------- |
| Negru Cosmin    | Backend Developer  | @cnegru38        |
| Răuțoiu Marco   | DevOps Engineer    | @RautoiuMarco    |
| Mihăiță Ingrid  | QA Engineer        | @Ingrid2911      |
| Popîrdă Eusebiu | Frontend Developer | @popardasebi3490 |

---

# 3. Arhitectura și Tehnologii

* **Backend:** Python FastAPI
* **Frontend:** C# ASP.NET Core Razor Pages
* **Database:** MongoDB

---

# 4. Setup Local (Cum rulăm proiectul)

## Prerequisites

Asigură-te că ai instalat următoarele:

* [.NET 8.0 SDK](https://dotnet.microsoft.com/download)
* [Python 3.x](https://www.python.org/downloads/)
* [MongoDB Community Edition](https://www.mongodb.com/try/download/community)
* [Visual Studio 2022](https://visualstudio.microsoft.com/)

### Python dependencies:

```bash
pip install fastapi uvicorn pymongo python-dotenv
```

---

## Step 1 — Start MongoDB

Deschide terminalul ca Administrator:

```bash
net start MongoDB
```

---

## Step 2 — Seed the Database (prima rulare)

Navighează în folderul backend:

```bash
python seed.py
```

---

## Step 3 — Start Backend API

```bash
python -m uvicorn main:app --reload
```

### API disponibil la:

* `http://localhost:8000`
* `http://localhost:8000/docs`

---

## Step 4 — Start Frontend

Deschide `MPIFrontend.sln` în Visual Studio 2022 și apasă:

```bash
F5
```

---

## Important:

MongoDB și backend-ul trebuie să ruleze înainte de frontend.

---

# Troubleshooting

## Windows Smart App Control

Dacă aplicația este blocată:

1. Caută **Smart App Control**
2. Deschide setările
3. Setează pe **Off**
4. Repornește Visual Studio

---

# Project Structure

```plaintext
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

# API Endpoints

| Method | URL               | Description                 |
| ------ | ----------------- | --------------------------- |
| GET    | `/`               | Health check                |
| GET    | `/api/games`      | Returns all games           |
| GET    | `/api/games/{id}` | Returns a single game by ID |
| POST   | `/api/games`      | Creates a new game          |
| PUT    | `/api/games/{id}` | Updates an existing game    |
| DELETE | `/api/games/{id}` | Deletes a game              |

---

## TODO

* Full Docker deployment support
* Linux compatibility improvements
