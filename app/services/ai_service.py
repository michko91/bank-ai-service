import logging

from langchain_groq import ChatGroq

from app.core.config import settings
from app.schemas.loan import AiRiskAnalysis, LoanRequest

logger = logging.getLogger(__name__)

class AIService:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0, # Für JSON-Output setzen wir die Kreativität auf 0
            model="llama-3.1-8b-instant",
            api_key=settings.GROQ_API_KEY
        )
        self.structured_llm = self.llm.with_structured_output(AiRiskAnalysis)

    async def analyze_loan_risk(self, loan: LoanRequest) -> AiRiskAnalysis:
        try:
            prompt = (
                f"Analysiere das Kreditrisiko für {loan.client_name}.\n"
                f"- Betrag: {loan.requested_amount} EUR\n"
                f"- Einkommen: {loan.monthly_income} EUR/Monat\n"
                f"- Berufserfahrung: {loan.employment_years} Jahre\n"
                f"- Bestehende Schulden: {'Ja' if loan.has_debts else 'Nein'}\n"
                "Erstelle eine fundierte Analyse basierend auf der Debt-To-Income Ratio."

            )
            analysis = await self.structured_llm.ainvoke(prompt)
            return analysis
        except Exception as e:
            logger.error(f"KI-Analyse mit Kontext fehlgeschlagen: {e}", exc_info=True)
            return AiRiskAnalysis(rating="F", reasoning="Fehler in der KI-Analyse", recommended_limit=0)

ai_service_instance = AIService()