from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.dialects.mysql import LONGBLOB
from database import Base


class Item(Base):
    __tablename__ = 'item'

    idItem = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(255))
    qtde = Column(Integer)
    precoVenda = Column(Float)
    precoCusto = Column(Float)
    imagem = Column(LONGBLOB)