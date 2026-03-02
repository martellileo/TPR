import random

# megasena
qtde = int(input("Informe a quantidade de jogos: "))
doisAcertos = 0
tresAcertos = 0
quatroAcertos = 0
cincoAcertos = 0
seisAcertos = 0

resultado = input("Entre com o resultado: ")
resultado = resultado.split() # separei em arrays
resultado = sorted(resultado) # ordenei a lista

for i in range(qtde):
    jogo = random.sample(range(1,11), k=6)
    jogo = sorted(['0'+str(x) if len(str(x))==1 else str(x)for x in jogo])

    acertos = len(set(jogo) & set(resultado))
    if(acertos == 2):
        doisAcertos += 1
    elif(acertos == 3):
        tresAcertos += 1
    elif(acertos == 4):
        quatroAcertos += 1
    elif(acertos == 5):
        cincoAcertos += 1
    elif(acertos == 6):
        seisAcertos += 1;
    print(f"Jogo {i+1}: {jogo} | Acertos: {acertos}")
    

print(f'Dois Acertos {doisAcertos}')
print(f'Tres Acertos {tresAcertos}')
print(f'Quatro Acertos {quatroAcertos}')
print(f'Cinco Acertos {cincoAcertos}')
print(f'Seis Acertos {seisAcertos}')