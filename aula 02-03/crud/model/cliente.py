class Cliente:

    def __init__(self):
        self._codcliente = 0
        self._nome = ''
        self._endereco = ''
        self._cidade = ''
        self._uf = ''
        self._cep = ''

    @property
    def codcliente(self):
        return self._codcliente

    @property
    def nome(self):
        return self._nome

    @property
    def endereco(self):
        return self._endereco
    
    @property
    def cidade(self):
        return self._cidade
    
    @property
    def uf(self):
        return self._uf
    
    @property
    def cep(self):
        return self._cep
    
# setter

    @codcliente.setter
    def codcliente(self, codcliente):
        self._codcliente = codcliente

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @cidade.setter
    def cidade(self, cidade):
        self._cidade = cidade

    @uf.setter
    def uf(self, uf):
        self._uf = uf

    @cep.setter
    def cep(self, cep):
        self._cep = cep

# csv

    def gravar_csv(self):
        return f'{self.codcliente};{self.nome};{self.endereco};{self.cidade};{self.uf};{self.cep}\n'

    def ler_csv(self, linha):
        dados = linha.split(';')
        self._codcliente = int(dados[0])
        self._nome = dados[1]
        self._endereco = dados[2]
        self._cidade = dados[3]
        self._uf = dados[4]
        self._cep = dados[5]
        return self
    
# str

    def __str__(self):
        return f'ID: {self._codcliente} | Nome: {self._nome} | Cidade: {self._cidade}-{self._uf}'