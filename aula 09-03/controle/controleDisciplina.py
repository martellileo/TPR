from controle.conectarbanco import Banco
from modelo.disciplina import *
from controle.controleGenerico import *


class ControleDisciplina(ControleGenerico):

    def incluirDisciplina(self, disciplina):
        self.incluir(disciplina)

    def alterarDisciplina(self, disciplina):
        self.alterar(disciplina)

    def deletarDisciplina(self, disciplina):
        self.delete(disciplina)

    def pesquisaCodigo(self, entrada: Disciplina):
        disciplina = self.procuraRegistro(entrada)
        retorno = Disciplina()
        if len(disciplina) >= 1:
            retorno = self.converte_disciplina(disciplina)
        return retorno

    def converte_disciplina(self, disciplina):
        retorno = Disciplina()
        retorno.iddisciplina = disciplina[0][0]
        retorno.nome = disciplina[0][1]
        retorno.cargahoraria = disciplina[0][2]
        return retorno

    def listarTodosRegistros(self, objeto):
        return self.listarTodos(objeto)

    def converteObjeto(self, entrada):
        disciplina = Disciplina()
        disciplina.iddisciplina = entrada[0]
        disciplina.nome = entrada[1]
        disciplina.cargahoraria = entrada[2]
        return disciplina

    def dadosJson(self, dados):
        retorno = {}
        retorno = {'iddisciplina': dados.disciplina,
                   'nome': dados.nome,
                   'cargahoraria': dados.endereco}
        return json.dumps(retorno)
