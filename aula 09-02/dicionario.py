# lista_numeros = [1,2,3,4,5]
# dicionario = {1:"um", 2:"dois"}
# lista = []

# dados = {
#     "Nome":"Leo Martelli",
#     "Cargo":"Estudante",
#     "Titulo":"Best fisherman 2011"
# }

# lista.append(dados)

# print(dados["Nome"])
# print(dados["Titulo"])

# for x,y in dados.items():
#     print(x,y)

materias = []

qntd = int(input("Digite a quantidade de disciplinas: "))

for i in range(qntd):
    print("--------------------")
    disciplina = input("Digite o nome da disciplina: ")
    qntdAulas = int(input("Digite a quantidade de aulas: "))
    diaSemana = input("Digite os dias da semana a ter aula(separar por espaço): ")

    dados = {
        "Disciplina":disciplina,
        "Qntd Aulas":qntdAulas,
        "Dia Semana":diaSemana.split() 
    }

    materias.append(dados)


for x in materias:
    print("--------------------")
    print(f"Nome da disciplina: {x["Disciplina"]}")
    print(f"Quantidade de aulas: {x["Qntd Aulas"]}")
    print(f"Dias da semana: {x["Dia Semana"]}")

print("--------------------")