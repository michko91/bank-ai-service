from app.schemas.loan import LoanRequest, LoanResponse
from app.services.ai_service import ai_service_instance


class CreditService:
    def __init__(self):
        from app.core.config import settings
        self.max_limit = settings.LOAN_MAX_LIMIT

    async def check_loan(self, loan: LoanRequest) -> LoanResponse:
        # KI-Analyse abrufen
        ai_result = await ai_service_instance.analyze_loan_risk(loan)

        # Logik basierend auf den Objekt_Attributen
        is_approved_by_limit = loan.requested_amount <= self.max_limit
        final_approval = is_approved_by_limit and ai_result.rating not in ["D", "F"]

        return LoanResponse(
            is_approved = final_approval,
            message = ai_result.reasoning,
            limit_used = self.max_limit,
            rating = ai_result.rating
        )

# Singleton-Instanz
credit_service_instance = CreditService()