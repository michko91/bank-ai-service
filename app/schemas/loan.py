from typing import Optional

from pydantic import BaseModel, Field


class LoanRequest(BaseModel):
    """Ausgehende Kreditabfrage"""
    client_name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description='Vollständiger Name des Kunden',
        examples=["Max Mustermann"]
    )

    requested_amount: float = Field(
        ...,
        gt=0,
        le=1000000,
        description="Kreditbetrag zwischen 1 und 1.000.000",
        examples=[5000.0]
    )

    monthly_income: float = Field(
        ...,
        gt=0,
        description="Netto-Einkommen pro Monat",
    )

    employment_years: int = Field(
        ...,
        ge=0,
        description="Jahre im aktuellen Job"
    )

    has_debts: bool = Field(
        ...,
        description="Sind Kreditschulden vorhanden"
    )

class LoanResponse(BaseModel):
    """Eingehende Kreditabfrage"""
    is_approved: bool
    message: str
    limit_used: float
    rating : str

class AiRiskAnalysis(BaseModel):
    rating: str = Field(description="Das Risiko-Rating von A bis E")
    reasoning: str = Field(description="Kurze Begründung für das Rating")
    recommended_limit: float = Field(description="Ein von der KI empfohlener Kreditrahmen")