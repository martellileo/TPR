from model.venda import Venda
import os

class VendaController:
    def __init__(self):
        self.arquivo = 'dados/vendas.csv'

    def cadastrar(self, venda):
        os.makedirs(os.path.dirname(self.arquivo), exist_ok=True)
        with open(self.arquivo, 'a', encoding='utf-8') as f:
            f.write(venda.gravar_csv())

    def listar_vendas(self):
        vendas = []
        if not os.path.exists(self.arquivo): return vendas
        with open(self.arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                if linha.strip():
                    vendas.append(Venda().ler_csv(linha))
        return vendas

    def buscar_por_id(self, codvenda):
        if not os.path.exists(self.arquivo): return None
        with open(self.arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                v = Venda().ler_csv(linha)
                if v.codvenda == codvenda:
                    return v
        return None