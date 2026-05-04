from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

class ItemVenda(Base):
    __tablename__ = 'itemvenda'

    idItemVenda = Column(Integer, primary_key=True, autoincrement=True)
    idVenda = Column(Integer, ForeignKey('venda.idVenda'))
    idItem = Column(Integer, ForeignKey('item.idItem'))
    quantidade = Column(Integer)
    precoUnitario = Column(Float)

    venda = relationship("Venda")
    item = relationship("Item")