from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.utils.rapidapi import fetch_funds

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/list")
def list_funds(fund_family: str, db: Session = Depends(get_db)):
    try:
        funds = fetch_funds(fund_family)
        return {"funds": funds}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))