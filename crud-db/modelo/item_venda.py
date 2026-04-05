from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class ItemVenda(Base):
    __tablename__ = 'itens_venda'

    id_venda = Column(Integer, ForeignKey('vendas.id_venda'), primary_key=True)
    id_produto = Column(Integer, ForeignKey('produtos.id_produto'), primary_key=True)
    qtde = Column(Integer, nullable=False)
    preco = Column(Float, nullable=False) 

    venda = relationship("Venda", back_populates="itens")
    produto = relationship("Produto")