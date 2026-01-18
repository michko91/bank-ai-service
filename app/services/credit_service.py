from app.schemas.loan import LoanRequest, LoanResponse
from app.services.ai_service import ai_service_instance


class CreditService:
    def __init__(self):
        from app.core.config import settings
        self.max_limit = settings.LOAN_MAX_LIMIT

    async def check_loan(self, loan: LoanRequest) -> LoanResponse:
        # 1. Harte Regelprüfung
        is_approved = loan.requested_amount <= self.max_limit

        # 2. KI-Zusatzprüfung
        ai_comment = await ai_service_instance.analyze_loan_risk(
            loan.client_name,
            loan.requested_amount
        )

        status_msg = "Genehmigt" if is_approved else "Abgelehnt"

        return LoanResponse(
            is_approved=is_approved,
            message=f"{status_msg}. KI-Einschätzung: {ai_comment}",
            limit_used=self.max_limit
        )

# Singleton-Instanz
credit_service_instance = CreditService()