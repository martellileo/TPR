from sqlalchemy import Column, Integer, String
from database import Base

class Cliente(Base):
    __tablename__ = 'clientes'
    id_cliente = Column(Integer, primary_key=True)
    nome = Column(String(100)) 
    endereco = Column(String(200)) 
    cidade = Column(String(100))
    uf = Column(String(2))
    cep = Column(String(9))