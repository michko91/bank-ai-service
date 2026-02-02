from requests import session
from sqlmodel import Session, select

from app.core.database import engine
from app.models.loan_table import LoanApplication
from app.schemas.loan import LoanRequest, LoanResponse
from app.services.ai_service import ai_service_instance


class CreditService:
    def __init__(self):
        from app.core.config import settings
        self.max_limit = settings.LOAN_MAX_LIMIT

    async def check_loan(self, loan: LoanRequest) -> LoanResponse:
        # 1. Hard Rule: Einkommens-Check (Bsp. 1000 €)
        if loan.monthly_income < 1000:
            return LoanResponse(
                is_approved=False,
                message = "Abgelehnt: Mindesteinkommen nicht erreicht.",
                limit_used = 0,
                rating = "F"
            )
        # 2. Hard Rule: Beitrags-Check
        if loan.requested_amount > self.max_limit:
            return LoanResponse(
                is_approved=False,
                message=f"Abgelehnt: Betrag übersteigt das absolute Limit von {self.max_limit}€.",
                rating="F"
            )
        # 3. Wenn die harten Regeln okay sind -> KI fragen
        ai_result = await ai_service_instance.analyze_loan_risk(loan)
        is_approved = ai_result.rating not in ["D", "F"]

        # 4. Datenbank-Speicherung
        new_app = LoanApplication(
            client_name=loan.client_name,
            requested_amount=loan.requested_amount,
            monthly_income=loan.monthly_income,
            rating=ai_result.rating,
            ai_reasoning=ai_result.reasoning,
            is_approved=is_approved
        )

        with Session(engine) as session:
            session.add(new_app)
            session.commit()
            session.refresh(new_app)

        return LoanResponse(
            is_approved = is_approved,
            message = ai_result.reasoning,
            limit_used = self.max_limit,
            rating = ai_result.rating
        )

    async def get_all_applications(self):
        with Session(engine) as session:
            statement = select(LoanApplication)
            results = session.exec(statement)
            return results.all()


# Singleton-Instanz
credit_service_instance = CreditService()