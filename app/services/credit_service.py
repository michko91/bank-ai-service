from app.core.config import settings
from app.schemas.loan import LoanRequest, LoanResponse


class CreditService:
    def __init__(self):
        self.max_limit = settings.LOAN_MAX_LIMIT

    def check_loan(self, loan: LoanRequest) -> LoanResponse:
        is_approved = loan.requested_amount <= self.max_limit

        msg = f"Glückwusnsch {loan.client_name}, der Betrag ist im Rahmen." if is_approved else \
            f"Leider abgelehnt. Unser Limit liegt bei {self.max_limit}."

        return LoanResponse(is_approved=is_approved, message=msg, limit_used=self.max_limit)

# Singleton-Instanz
credit_service_instance = CreditService()