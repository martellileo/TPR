from database import Session
from modelo.cliente import Cliente

class ClienteController:
    def cadastrar(self, nome, endereco, cidade, uf, cep):
        with Session() as session:
            novo = Cliente(nome=nome, endereco=endereco, cidade=cidade, uf=uf, cep=cep)
            session.add(novo)
            session.commit()
            session.refresh(novo)
            return novo

    def buscar_por_id(self, id_cliente):
        with Session() as session:
            return session.query(Cliente).filter_by(id_cliente=id_cliente).first()

    def listar_todos(self):
        with Session() as session:
            return session.query(Cliente).all()