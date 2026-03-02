from model.produto import Produto
import os

class ProdutoController:

    def __init__(self):
        self.lista_produtos = []
        self.nome_arquivo = 'dados/produtos.csv'

    def cadastrar(self, produto):
        self.lista_produtos.append(produto)

    def remover(self, produto):
        self.lista_produtos.remove(produto)

    def atualizar(self, produto_atualizado):
        for i, p in enumerate(self.lista_produtos):
            if p.codproduto == produto_atualizado.codproduto:
                self.lista_produtos[i] = produto_atualizado
                return True
        return False

    def listar_todos(self):
        return self.lista_produtos

    def buscar(self, codproduto):
        for produto in self.lista_produtos:
            if produto.codproduto == codproduto:
                return produto
        return None
    
    def salvar_csv(self):
        os.makedirs(os.path.dirname(self.nome_arquivo), exist_ok=True)
        with open(self.nome_arquivo, 'w') as f:
            for p in self.lista_produtos:
                f.write(p.gravar_csv())
        return True
    
    def carregar_csv(self):
        self.lista_produtos = []
        if not os.path.exists(self.nome_arquivo):
            with open(self.nome_arquivo, 'w') as f:
                pass
        else:
            with open(self.nome_arquivo, 'r') as f:
                for linha in f:
                    if linha.strip():
                        p = Produto()
                        p.ler_csv(linha)
                        self.lista_produtos.append(p)
                return True
