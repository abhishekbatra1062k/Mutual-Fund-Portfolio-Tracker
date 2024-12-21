from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models.user import User
from app.models.portfolio import Portfolio

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/view")
def view_portfolio(user_id: int, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    portfolio = db.query(Portfolio).filter(Portfolio.user_id == user_id).all()
    return {"portfolio": [{"fund_name": p.fund_name, "units": p.units, "purchase_price": p.purchase_price} for p in portfolio]}


@router.post("/update")
def update_portfolio(user_id: int, fund_name: str, units: float, purchase_price: float, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    new_portfolio = Portfolio(user_id=user_id, fund_name=fund_name, units=units, purchase_price=purchase_price)
    db.add(new_portfolio)
    db.commit()
    db.refresh(new_portfolio)
    return {"status": "Portfolio updated successfully", "portfolio": {
        "fund_name": fund_name,
        "units": units,
        "purchase_price": purchase_price
    }}

