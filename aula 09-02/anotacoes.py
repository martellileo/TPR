import random

# somar 100
qtde = int(input("Informe a quantidade de jogos: "))
for i in range(qtde):
    jogo = random.sample(range(1,61), k=6)
    jogo = [str(x+100)[1:3] for x in jogo]
    jogo = sorted(jogo)
    print(" ".join(jogo))

#----------------------------------

# adicionar 0 na frente
qtde = int(input("Informe a quantidade de jogos: "))
for i in range(qtde):
    jogo = random.sample(range(1,61), k=6)
    jogo = ['0'+str(x) if len(str(x))==1 else str(x)for x in jogo]
    jogo = sorted(jogo)
    print(" ".join(jogo))

#----------------------------------

# adicionar na lista
lista_frutas = ['maça', 'banana', 'pera', 'abacaxi', 'melancia', 'uva']
lista_frutas.append('tamarindo')
lista_frutas.sort()
for i in lista_frutas:
    print(i)
if 'maça' in lista_frutas:
    print("existe")

