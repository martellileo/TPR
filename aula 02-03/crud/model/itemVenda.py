class ItemVenda:

    def __init__(self):
        self._codvenda = 0
        self._codproduto = 0
        self._qntd = 0
        self._valor = 0

    @property
    def codvenda(self):
        return self._codvenda
    
    @property
    def codproduto(self):
        return self._codproduto
    
    @property
    def qntd(self):
        return self._qntd
    
    @property
    def valor(self):
        return self._valor
    
# setter

    @codvenda.setter
    def codvenda(self, codvenda):
        self._codvenda = codvenda

    @codproduto.setter
    def codproduto(self, codproduto):
        self._codproduto = codproduto

    @qntd.setter
    def qntd(self, qntd):
        self._qntd = qntd

    @valor.setter
    def valor(self, valor):
        self._valor = valor

# csv

    def gravar_csv(self):
        return f'{self.codvenda};{self.codproduto};{self.qntd};{self.valor}\n'

    def ler_csv(self, linha):
        dados = linha.split(';')
        self._codvenda = int(dados[0])
        self._codproduto = int(dados[1])
        self._qntd = int(dados[2])
        self._valor = float(dados[3])
        return self
    
# str
    def __str__(self):
        return f'Venda: {self._codvenda} | Prod: {self._codproduto} | Qtd: {self._qntd} | Unit: R$ {self._valor:.2f}'