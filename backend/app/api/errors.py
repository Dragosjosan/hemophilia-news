from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.services.cursors import InvalidCursorError


async def _invalid_cursor(_: Request, __: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, content={"detail": "Invalid cursor"}
    )


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(InvalidCursorError, _invalid_cursor)
