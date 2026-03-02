class Venda:

    def __init__(self):
        self._codvenda = 0
        self._data = ''
        self._valor_total = ''
        self._codcliente = 0

    @property
    def codvenda(self):
        return self._codvenda
    
    @property
    def data(self):
        return self._data
    
    @property
    def valor_total(self):
        return self._valor_total
    
    @property
    def codcliente(self):
        return self._codcliente
    

# setter

    @codvenda.setter
    def codvenda(self, codvenda):
        self._codvenda = codvenda

    @data.setter
    def data(self, data):
        self._data = data

    @valor_total.setter
    def valor_total(self, valor_total):
        self._valor_total = valor_total

    @codcliente.setter
    def codcliente(self, codcliente):
        self._codcliente = codcliente        

# csv

    def gravar_csv(self):
        return f'{self.codvenda};{self.data};{self.valor_total};{self.codcliente}\n'

    def ler_csv(self, linha):
        dados = linha.split(';')
        self._codproduto = int(dados[0])
        self._data = dados[1]
        self._valor_total = float(dados[2])
        self._codcliente = int(dados[3])
        return self
    
    
# str

    def __str__(self):
        return f'Id: {self._codproduto} | Data: {self._nome} | R$ {self._valor_total} | CodCliente {self._codcliente}'