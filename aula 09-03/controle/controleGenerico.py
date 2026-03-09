from controle.conectarbanco import *
import json
import datetime
import os


class ControleGenerico:

    def __init__(self):
        with open('configura.txt', encoding='utf-8') as f:
            dados = f.read().split(",")

        self.ob = Banco()
        self.ob.configura(ho=dados[0],db=dados[1],us=dados[2],se=dados[3],po=int(dados[4]))

    def incluir(self,objeto):
        self.ob.abrirConexao()
        sql = "insert into {} ".format(objeto.tabelaBanco)+'('
        sql+= '{}'.format(objeto.lista)
        sql+= ') values ({})'.format(objeto.dadosInserir)

        try:
           self.ob.execute(sql)
           self.ob.gravar()
        except:
           print("Houve um erro")
           self.ob.descarte()

    def alterar(self,objeto):
        self.ob.abrirConexao();
        sql = "update {} ".format(objeto.tabelaBanco)
        sql += 'set {}'.format(objeto.dadosUpdate)

        try:
           self.ob.execute(sql)
           self.ob.gravar()
        except:
           print("Houve um erro")
           self.ob.descarte()

    def delete(self, objeto):
        self.ob.abrirConexao();
        sql = "delete from {} ".format(objeto.tabelaBanco)
        sql += objeto.dadosDelete

        try:
            self.ob.execute(sql)
            self.ob.gravar()
        except:
            print("Houve um erro")
            self.ob.descarte()

    def procuraRegistro(self,objeto):
        self.ob.abrirConexao()
        objeto = self.ob.selectQuery(objeto.dadosPesquisa)
        return objeto

    def apagar(self,entrada):
        self.ob.abrirConexao();
        sql = "delete from aluno where idaluno = {}".format(entrada)
        self.ob.execute(sql)
        self.ob.gravar()

    def listarTodos(self,objeto):
        self.ob.abrirConexao()
        dados = self.ob.selectQuery("select * from {}".format(objeto.tabelaBanco))
        return dados




