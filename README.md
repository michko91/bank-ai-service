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
```text
bank-ai-service/
├── app/
│   ├── api/        # Endpunkte & Router
│   ├── core/       # Config, Datenbank-Setup & Exceptions
│   ├── models/     # SQLModel Datenbank-Tabellen
│   ├── schemas/    # Pydantic Modelle für API Validation
│   └── services/   # Business Logic & AI-Integration
├── Dockerfile      # Backend Container-Definition
├── docker-compose.yml # Multi-Container Orchestrierung
├── main.py         # Entrypoint der App
└── .env            # Umgebungsvariablen (API Keys, DB-URL)

## 🚦 Schnellstart

1. **Repository klonen**
2. **Umgebungsvariablen konfigurieren:** Erstelle eine `.env` Datei im Hauptverzeichnis mit folgendem Inhalt:
   ```env
   GROQ_API_KEY=dein_key_hier
   DATABASE_URL=postgresql://user:password@db:5432/bank_db
