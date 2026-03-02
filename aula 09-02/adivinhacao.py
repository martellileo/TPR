import random

# jogo de adivinhação
vidas = 7
sorteado = random.randint(1, 100)
tentativas = []
nome = input("Digite o seu nome: ")
while vidas > 0:
    entrada = int(input("Digite um numero entre 1 a 100: "))
    if sorteado != entrada:
        vidas -= 1
        if entrada < sorteado:
            print(f"O número sorteado é maior que {entrada} | {nome}, {vidas} vidas restantes!")
            tentativas.append(entrada)
        elif entrada > sorteado:
            print(f"O número sorteado é menor que {entrada} | {nome}, {vidas} vidas restantes!")
            tentativas.append(entrada)
    else:
        tentativas.append(entrada)
        print(f"{nome}, numero {entrada} correto, parabens! | Acerto em {len(tentativas)} tentativas")
        print(entrada)
        break
    if vidas == 0:
        print(f"{nome}, você perdeu! O número sorteado era: {sorteado}!")

print(f"Suas tentativas foram: {tentativas}")