def gravar(ano, dadosGravar):
    with open(f'aula 23-02/{ano}.txt', 'w') as f:
        for i in dadosGravar:
            f.write(i+'\n')

with open('aula 23-02/megasena.txt') as f:
    dados = f.read().split("\n")

ano = ''
lista = []
for x in dados:
    if ano != x[12:17]:
        if len(lista)>0:
            gravar(ano, lista)
        ano=x[12:17]
        lista=[]
        lista.append(x)
    else:
        lista.append(x)
        gravar(ano, lista)