# 🏦 Bank-AI Enterprise Service

Ein modernes Kreditprüfungssystem, das harte Geschäftsregeln mit künstlicher Intelligenz (Groq/Llama 3) kombiniert, um Kreditanträge in Echtzeit zu bewerten und revisionssicher in einer PostgreSQL-Datenbank zu speichern.

## 🚀 Status Quo
Das System ist vollständig containerisiert und verfügt über eine funktionierende End-to-End-Pipeline:
- **API:** FastAPI mit asynchronem Lifespan-Management.
- **AI-Integration:** Automatisierte Risikoanalyse via Groq Cloud API.
- **Persistence:** SQLModel (ORM) mit einer PostgreSQL-Datenbank im Docker-Verbund.
- **Infrastruktur:** Orchestrierung über Docker Compose.

## 🛠 Tech Stack
* **Backend:** Python 3.11, FastAPI
* **Database:** PostgreSQL 15
* **ORM:** SQLModel (Pydantic + SQLAlchemy)
* **AI:** Groq SDK (Llama 3 Modelle)
* **DevOps:** Docker, Docker Compose
* **Validation:** Pydantic V2 Settings & Schemas

## 🏗 Projektstruktur
- **app/**: Core-Logik, Models, Schemas und Services.
- **Dockerfile**: Backend Container-Definition.
- **docker-compose.yml**: Orchestrierung von Backend und Datenbank.
- **main.py**: Zentraler Entrypoint der Anwendung.

## 🚦 Schnellstart

1. **Repository klonen**
2. **Umgebungsvariablen konfigurieren:** Erstelle eine `.env` Datei im Hauptverzeichnis mit folgendem Inhalt:
   ```env
   GROQ_API_KEY=dein_key_hier
   DATABASE_URL=postgresql://user:password@db:5432/bank_db
3. **Container starten:** Führe diesen Befehl im Projektverzeichnis aus, um das Image zu bauen und alle Dienste zu starten:
   ```env
   docker compose up --build
4. **API & Monitoring:**
   ```env
   - Backend-Basis: http://localhost:8000
   - Interaktive Dokumentation (Swagger UI): http://localhost:8000/docs
   - Admin-Endpoint (Gespeicherte Anträge): http://localhost:8000/applications

## 🗺 Roadmap
* [x] **Backend-Core**: FastAPI Setup mit asynchroner Architektur und Exception-Handling.
* [x] **KI-Integration**: Risikoanalyse-Logik via Groq Cloud (Llama 3).
* [x] **Infrastruktur**: Vollständige Containerisierung mit Docker & Docker Compose.
* [x] **Persistenz**: PostgreSQL-Anbindung und automatische Tabellen-Initialisierung via SQLModel.
* [ ] **Frontend (Next Step)**: Entwicklung eines modernen Dashboards mit React, Vite & Tailwind CSS.
* [ ] **Features**: Implementierung von Such-, Filter- und Löschfunktionen für Kreditanträge.
* [ ] **Security**: Absicherung des Admin-Bereichs mittels JWT-Authentifizierung.
