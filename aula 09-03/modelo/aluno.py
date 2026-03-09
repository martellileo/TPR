import datetime

class Aluno:

    def __init__(self):
        self.__idaluno = 0
        self.__nome=""
        self.__endereco=""
        self.__nascimento=""
        self.__cidade=""
        self.__uf = ""
        self.__cep = ""
        self.__lista='nome,endereco,nascimento,cidade,uf,cep'

        self.__dadosInserir=""
        self.__dadosUpdate=""
        self.__dadosDelete=""
        self.__dadosPesquisa=""
        self.__tabelaBanco = 'aluno'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        self.__dadosInserir = f"'{self.nome}','{self.endereco}','{self.nascimento}','{self.cidade}','{self.uf}','{self.cep}'"
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = ("nome='{}',endereco='{}',nascimento='{}',cidade='{}',uf='{}',cep='{}' where idaluno={}").format(self.nome,
                                                                                                                              self.endereco,
                                                                                                                              self.nascimento,
                                                                                                                              self.cidade,
                                                                                                                              self.uf,
                                                                                                                              self.cep,                                                                                                      self.idaluno)
        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where idaluno={}".format(self.idaluno)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from aluno where idaluno={}".format(self.idaluno)
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def idaluno(self):
        return self.__idaluno

    @idaluno.setter
    def idaluno(self, entrada):
        self.__idaluno = entrada

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,entrada):
        self.__nome=entrada

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, entrada):
        self.__endereco = entrada

    @property
    def nascimento(self):
        return self.__nascimento

    @nascimento.setter
    def nascimento(self, entrada:str):
        self.__nascimento = entrada

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, entrada):
        self.__cidade = entrada

    @property
    def uf(self):
        return self.__uf

    @uf.setter
    def uf(self, entrada):
        self.__uf = entrada

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, entrada):
        self.__cep = entrada

    def converte_data_str(self, data):
        if isinstance(data, datetime.date):
            return data.strftime("%d/%m/%Y")
        return str(data)

    def __repr__(self):
        if isinstance(self.__nascimento,str):
           return  self.__nome+' '+self.__endereco+' '+self.__nascimento+' '+self.__cidade+' '+self.__uf+' '+self.__cep
        if isinstance(self.__nascimento,datetime.date):
           return self.__nome + ' ' + self.__endereco + ' ' +self.converte_data_str(self.__nascimento) + ' ' + self.__cidade + ' ' + self.__uf + ' ' + self.__cep

        return '-----'