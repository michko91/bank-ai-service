from typing import Annotated

from fastapi import FastAPI, Depends

from app.core.config import settings
from app.core.exceptions import setup_exception_handlers
from app.schemas.loan import LoanResponse, LoanRequest
from app.services.credit_service import CreditService, credit_service_instance

app = FastAPI(title=settings.PROJECT_NAME)

# Exception Handler registrieren
setup_exception_handlers(app)

# Provider gibt nur das fertige Singleton zurück
def get_credit_service() -> CreditService:
    return credit_service_instance

@app.post("/apply", response_model=LoanResponse)
async def apply_for_loan(
        loan_data: LoanRequest,
        service: Annotated[CreditService, Depends(get_credit_service)]
):
        return await service.check_loan(loan_data)