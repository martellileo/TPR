def gravar_dados(dadosGravar):
    with open('aula 23-02/saida.txt', 'w') as f:
        for i in dadosGravar:
            i = " ".join(i)
            f.write(i+'\n')

with open('aula 23-02/megasena.txt') as f:
    dados = f.read().split("\n")

dezena = (input("Qual dezena deseja gravar arquivo: "))

lista_gravar = []

for x in dados:
    if x != '':
        x = x.split()
        lista_numeros = x[2:]
        if dezena in lista_numeros:
            lista_gravar.append(x)

gravar_dados(lista_gravar)
