from sqlalchemy import Column, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base
from datetime import date


class Venda(Base):
    __tablename__ = 'vendas'

    id_venda = Column(Integer, primary_key=True)
    valor_total = Column(Float, default=0.0)
    data = Column(Date, default=date.today)
    id_cliente = Column(Integer, ForeignKey('clientes.id_cliente'))

    cliente = relationship("Cliente")
    itens = relationship("ItemVenda", back_populates="venda", cascade="all, delete-orphan")