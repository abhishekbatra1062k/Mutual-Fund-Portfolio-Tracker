from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

class Portfolio(Base):
    __tablename__ = "portfolios"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    fund_name = Column(String, nullable=False)
    units = Column(Float, nullable=False)
    purchase_price = Column(Float, nullable=False)

    user = relationship("User", back_populates="portfolios")
