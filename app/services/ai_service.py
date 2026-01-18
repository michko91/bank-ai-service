import logging

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from app.core.config import settings

logger = logging.getLogger(__name__)

class AIService:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0.5,
            model="llama-3.1-8b-instant",
            api_key=settings.GROQ_API_KEY
        )
        logger.info("AIService mit Groq initialisiert.")

    async def analyze_loan_risk(self, name: str, amount: float) -> str:
        try:
            prompt = ChatPromptTemplate.from_messages(
                messages=[("system", "Du bist ein Risiko-Analyst einer Bank. Antworte kurz und präzise."),
                ("user", "Analysiere das Risiko für: Kunde {kunde}, Betrag {betrag} EUR.")])

            chain = prompt | self.llm
            response = await chain.ainvoke({"kunde": name, "betrag": amount})

            return response.content
        except Exception as e:
            logger.error(f"Groq Fehler {e}", exc_info=True)
            return "KI-Risikoanalyse momentan nicht verfügbar."

ai_service_instance = AIService()