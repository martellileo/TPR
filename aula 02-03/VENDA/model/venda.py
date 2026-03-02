class Venda:
    
    def __init__(self):
        self._codvenda = 0
        self._data = ''
        self._valor_total = 0.0
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

    @codvenda.setter
    def codvenda(self, valor):
        self._codvenda = valor

    @data.setter
    def data(self, valor):
        self._data = valor

    @valor_total.setter
    def valor_total(self, valor):
        self._valor_total = valor

    @codcliente.setter
    def codcliente(self, valor):
        self._codcliente = valor

    def gravar_csv(self):
        return f'{self.codvenda};{self.data};{self.valor_total};{self.codcliente}\n'

    def ler_csv(self, linha):
        dados = linha.strip().split(';')
        self._codvenda = int(dados[0])
        self._data = dados[1]
        self._valor_total = float(dados[2])
        self._codcliente = int(dados[3])
        return self

    def __str__(self):
        return f'ID Venda: {self._codvenda} | Data: {self._data} | Total: R$ {self._valor_total:.2f} | Cód. Cliente: {self._codcliente}'