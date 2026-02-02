from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from sqlmodel import SQLModel, Field


class LoanApplication(SQLModel, table=True):
    # ID wird automatisch generiert
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)

    # Nutzerdaten
    client_name: str
    requested_amount: float
    monthly_income: float

    # KI-Egebnisse
    rating: str
    ai_reasoning: str
    is_approved: bool

    # Metadaten für die Bank
    created_at: datetime = Field(default_factory=datetime.utcnow)

    __tablename__ = "loan_applications"