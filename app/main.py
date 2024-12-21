from fastapi import FastAPI
from app.routers import auth, funds, portfolio

app = FastAPI(title="Mutual Fund Broker Web App")

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(funds.router, prefix="/funds", tags=["Funds"])
app.include_router(portfolio.router, prefix="/portfolio", tags=["Portfolio"])