from controle.controleAluno import ControleAluno
from controle.controleDisciplina import ControleDisciplina
from modelo.aluno import Aluno
from modelo.disciplina import Disciplina
from datetime import datetime

daoAluno = ControleAluno()
daoDisc = ControleDisciplina()

print('Conectado')

# -----------------------
# INSERINDO ALUNOS
# -----------------------

print('Incluindo alunos')

aluno1 = Aluno()
aluno1.nome = 'Joao Silva'
aluno1.endereco = 'Rua 1'
aluno1.cidade = 'Belo Horizonte'
aluno1.uf = 'MG'
aluno1.cep = '30100000'
aluno1.nascimento = '2000-05-10'

daoAluno.incluir(aluno1)

aluno2 = Aluno()
aluno2.nome = 'Maria Souza'
aluno2.endereco = 'Rua 2'
aluno2.cidade = 'Sao Paulo'
aluno2.uf = 'SP'
aluno2.cep = '01000000'
aluno2.nascimento = '1999-08-20'

daoAluno.incluir(aluno2)


# -----------------------
# INSERINDO DISCIPLINAS
# -----------------------

print('Incluindo disciplinas')

disc1 = Disciplina()
disc1.nome = 'Banco de Dados'
disc1.cargahoraria = '60h'

daoDisc.incluir(disc1)

disc2 = Disciplina()
disc2.nome = 'Programacao Python'
disc2.cargahoraria = '80h'

daoDisc.incluir(disc2)


# -----------------------
# LISTANDO ALUNOS
# -----------------------

print('\nLista de alunos')
listaAluno = daoAluno.listarTodos(Aluno())

for x in listaAluno:
    aluno = daoAluno.converteObjeto(x)
    print(aluno)

# -----------------------
# LISTANDO DISCIPLINAS
# -----------------------
print('\nLista de disciplinas')
listaDisciplina = daoDisc.listarTodos(Disciplina())

for x in listaDisciplina:
    disc = daoDisc.converteObjeto(x)
    print(disc)