from sqlalchemy import Column, Integer, Date, Float, String
from database import Base

class Venda(Base):
    __tablename__ = 'venda'

    idVenda = Column(Integer, primary_key=True)
    data = Column(Date)
    precoTotal = Column(Float)
    formaPagamento = Column(String(50))
    dataPagamento = Column(Date)