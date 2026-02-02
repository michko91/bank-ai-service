from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)

def init_db():
    #Funktion zum erstellen der Tabellen in Postgres
    SQLModel.metadata.create_all(engine)

def get_Session():
    with Session(engine) as session:
        yield session