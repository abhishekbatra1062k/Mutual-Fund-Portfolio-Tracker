from pydantic import BaseModel

class PortfolioBase(BaseModel):
    fund_name: str
    units: float
    purchase_price: float

class PortfolioCreate(PortfolioBase):
    pass

class PortfolioOut(PortfolioBase):
    id: int

    class Config:
        orm_mode = True
