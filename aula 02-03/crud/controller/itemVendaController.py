from model.itemVenda import ItemVenda
import os

class ItemVendaController:
    def __init__(self):
        self.arquivo = 'dados/itens_venda.csv'

    def cadastrar(self, item):
        os.makedirs(os.path.dirname(self.arquivo), exist_ok=True)
        with open(self.arquivo, 'a', encoding='utf-8') as f:
            f.write(item.gravar_csv())

    def listar_itens_da_venda(self, codvenda):
        itens = []
        if not os.path.exists(self.arquivo): return itens
        with open(self.arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                if linha.strip():
                    it = ItemVenda().ler_csv(linha)
                    if it.codvenda == codvenda:
                        itens.append(it)
        return itens