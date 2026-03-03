class Produto:

    def __init__(self):
        self._id = 0
        self._nome = ''
        self._preco = 0
        self._quantidade = 0

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    @property
    def quantidade(self):
        return self._quantidade

# setter

    @id.setter
    def id(self, id):
        self._id = id

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @preco.setter
    def preco(self, preco):
        if preco > 0:
            self._preco = preco
        else:
            self._preco = -1

    @quantidade.setter
    def quantidade(self, quantidade):
        if quantidade > 0:
            self._quantidade = quantidade
        else:
            self._quantidade = -1