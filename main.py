from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, Depends

from app.core.config import settings
from app.core.database import init_db
from app.core.exceptions import setup_exception_handlers
from app.schemas.loan import LoanResponse, LoanRequest
from app.services.credit_service import CreditService, credit_service_instance

def get_credit_service() -> CreditService:
    return credit_service_instance

@asynccontextmanager
async def lifespan(app: FastAPI):
    #Phase 1: Startvorgang
    print("🚀 Anwendung startet....")
    try:
        init_db()
        print("✅ Datenbank-Tabellen erfolgreich initialisiert.")
    except Exception as e:
        print(f"❌ Fehler bei der DB-Initialisierung: {e}")

    yield

    #Phase 2: Herunterfahren
    print("🛑 System wird sauber heruntergefahren...")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    lifespan=lifespan
)

# Exception Handler registrieren
setup_exception_handlers(app)

@app.post("/apply", response_model=LoanResponse)
async def apply_for_loan(
        loan_data: LoanRequest,
        service: Annotated[CreditService, Depends(get_credit_service)]
):
        return await service.check_loan(loan_data)

@app.get("/")
async def root():
    return {
        "status": "online",
        "service": "Bank-AI",
        "database": "connected"
    }
@app.get("/applications")
async def get_applications(
        service: Annotated[CreditService, Depends(get_credit_service)]
):
    return await service.get_all_applications()


