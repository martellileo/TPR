class Disciplina:

    def __init__(self):
        self.__iddisciplina = 0
        self.__nome = ""
        self.__cargahoraria = ""
        self.__lista = 'nome,cargahoraria'

        self.__dadosInserir = ""
        self.__dadosUpdate = ""
        self.__dadosDelete = ""
        self.__dadosPesquisa = ""
        self.__tabelaBanco = 'disciplina'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        self.__dadosInserir = f"'{self.nome}','{self.cargahoraria}'"
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = ("nome='{}',cargahoraria='{}' where iddisciplina={}").format(
            self.nome,
            self.cargahoraria,
            self.iddisciplina
        )
        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where iddisciplina={}".format(self.iddisciplina)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from disciplina where iddisciplina={}".format(self.iddisciplina)
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def iddisciplina(self):
        return self.__iddisciplina

    @iddisciplina.setter
    def iddisciplina(self, entrada):
        self.__iddisciplina = entrada

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, entrada):
        self.__nome = entrada

    @property
    def cargahoraria(self):
        return self.__cargahoraria

    @cargahoraria.setter
    def cargahoraria(self, entrada):
        self.__cargahoraria = entrada

    def __repr__(self):
        return f"{self.__nome} {self.__cargahoraria}"