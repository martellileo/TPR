from model.cliente import Cliente
import os

class ClienteController:
    def __init__(self):
        self.lista_clientes = []
        self.nome_arquivo = 'dados/clientes.csv'

    def cadastrar(self, cliente):
        self.lista_clientes.append(cliente)

    def atualizar(self, cliente_atualizado):
        for i, p in enumerate(self.lista_clientes):
            if p.codcliente == cliente_atualizado.codcliente:
                self.lista_clientes[i] = cliente_atualizado
                return True
        return False

    def remover(self, cliente):
        self.lista_clientes.remove(cliente)

    def listar_todos(self):
        return self.lista_clientes
    
    def buscar(self, codcliente):
        for cliente in self.lista_clientes:
            if  cliente.codcliente == codcliente:
                return cliente
        return None
    
    def salvar_csv(self):
        os.makedirs(os.path.dirname(self.nome_arquivo), exist_ok=True)
        with open(self.nome_arquivo, 'w') as f:
            for p in self.lista_clientes:
                f.write(p.gravar_csv())
        return True
    
    def carregar_csv(self):
        self.lista_clientes = []
        if not os.path.exists(self.nome_arquivo):
            with open(self.nome_arquivo, 'w') as f:
                pass
        else:
            with open(self.nome_arquivo, 'r') as f:
                for linha in f:
                    if linha.strip():
                        c = Cliente()
                        c.ler_csv(linha)
                        self.lista_clientes.append(c)
                return True