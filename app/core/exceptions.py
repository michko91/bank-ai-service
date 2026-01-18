import logging

from fastapi import FastAPI, Request, status
from pydantic import ValidationError
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)

def setup_exception_handlers(app: FastAPI):

    @app.exception_handler(ValidationError)
    async def validation_exception_handler(request: Request, exc: ValidationError):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_FORMAT,
            content={
                "error_code": "VALIDATION_ERROR",
                "message": "Eingabedaten ungültig",
                "details": exc.errors(),
            },
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logger.exception(f"Globaler Fehler abgefangen: {exc}", exc_info=True)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "error_code": "INTERNAL_SERVER_ERROR",
                "message": "Ein unerwarteter Fehler ist aufgetreten."
            },
        )