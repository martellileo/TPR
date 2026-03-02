class Produto:

    def __init__(self):
        self._codproduto = 0
        self._nome = ''
        self._preco = 0

    @property
    def codproduto(self):
        return self._codproduto

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

# setter

    @codproduto.setter
    def codproduto(self, codproduto):
        self._codproduto = codproduto

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @preco.setter
    def preco(self, preco):
        if preco > 0:
            self._preco = preco
        else:
            self._preco = -1

# csv

    def gravar_csv(self):
        return f'{self.codproduto};{self.nome};{self.preco}\n'

    def ler_csv(self, linha):
        dados = linha.split(';')
        self._codproduto = int(dados[0])
        self._nome = dados[1]
        self._preco = float(dados[2])
        return self
    
# str

    def __str__(self):
        return f'Id: {self._codproduto} | Produto: {self._nome} | R$ {self._preco}'