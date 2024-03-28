from app.routes.user_router import router as user_router
from fastapi import FastAPI

app: FastAPI = FastAPI(
    title="GestorContabil API",
    version="0.1.0"
)

app.include_router(user_router)
