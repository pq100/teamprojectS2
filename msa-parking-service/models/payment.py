from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Payment(Base):
    __tablename__ = 'payment'

    mno = Column(Integer, primary_key=True, autoincrement=True, index=True)
    payid = Column(String(30), nullable=False)
    payment = Column(String(50), nullable=False)
    paydate = Column(String(50), nullable=False)
    carnum = Column(String(15), nullable=False)
