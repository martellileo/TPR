from database import Session
from modelo.produto import Produto

class ProdutoController:
    def cadastrar(self, nome, qtde, preco):
        with Session() as session:
            novo = Produto(nome=nome, qtde=qtde, preco=preco)
            session.add(novo)
            session.commit()
            return novo

    def listar_todos(self):
        with Session() as session:
            return session.query(Produto).all()

    def listar_todos(self):
        with Session() as session:
            return session.query(Produto).all()