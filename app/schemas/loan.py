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

class LoanResponse(BaseModel):
    """Eingehende Kreditabfrage"""
    is_approved: bool
    message: str
    limit_used: float