from sqlalchemy import Column, Integer, String, Float
from database import Base

class Produto(Base):
    __tablename__ = 'produtos'
    id_produto = Column(Integer, primary_key=True)
    nome = Column(String(150))  
    qtde = Column(Integer)
    preco = Column(Float)