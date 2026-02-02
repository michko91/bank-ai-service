# Python-Image
FROM python:3.11-slim

# Arbeitsverzeichnis im Container
WORKDIR /app

# System-Abhängigkeiten für Postgres installieren
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Zuerst nur die Anforderungen kopieren (Docker-Caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Den Rest des Codes kopieren
COPY . .

# Den Port für FastApi freigeben
EXPOSE 8000

# Befehl zum starten der App
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]