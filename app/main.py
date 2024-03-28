from app.routes.user_router import router as user_router
from app.routes.expense_router import router as expense_router
from app.routes.revenue_router import router as revenue_router
from fastapi import FastAPI

app: FastAPI = FastAPI(
    title="GestorContabil API",
    version="0.1.0"
)

app.include_router(user_router)
app.include_router(expense_router)
app.include_router(revenue_router)
