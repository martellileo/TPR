from controle.conectarbanco import Banco
from modelo.aluno import *
from controle.controleGenerico import *


class ControleAluno(ControleGenerico):

    def incluirAluno(self, aluno):
        self.incluir(aluno)

    def alterarAluno(self, aluno):
        self.alterar(aluno)

    def deletarAluno(self, aluno):
        self.delete(aluno)

    def pesquisaCodigo(self, entrada: Aluno):
        aluno = self.procuraRegistro(entrada)
        retorno = Aluno()
        if len(aluno) >= 1:
            retorno = self.converte_aluno(aluno)
        return retorno

    def converte_aluno(self, aluno):
        retorno = Aluno()
        retorno.idaluno = aluno[0][0]
        retorno.nome = aluno[0][1]
        retorno.endereco = aluno[0][2]
        retorno.nascimento = aluno[0][3]
        retorno.cidade = aluno[0][4]
        retorno.uf = aluno[0][5]
        retorno.cep = aluno[0][6]
        return retorno

    def listarTodosRegistros(self, objeto):
        return self.listarTodos(objeto)

    def converteObjeto(self, entrada):
        aluno = Aluno()
        aluno.idaluno = entrada[0]
        aluno.nome = entrada[1]
        aluno.endereco = entrada[2]
        aluno.nascimento = entrada[3]
        aluno.cidade = entrada[4]
        aluno.cep = entrada[5]
        aluno.cep = entrada[6]
        return aluno

    def dadosJson(self, dados):
        retorno = {}
        retorno = {'idaluno': dados.idaluno,
                   'nome': dados.nome,
                   'endereco': dados.endereco,
                   'cidade': dados.cidade,
                   'uf': dados.uf,
                   'cep': dados.cep,
                   'nascimento': '{}'.format(dados.nascimento)}
        return json.dumps(retorno)
