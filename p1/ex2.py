arquivo = "arquivo2.txt"

with open(arquivo, 'r') as f:
    texto = f.read()

palavras = texto.split()

maior = 0
for p in palavras:
    contador = 0
    for letra in p:
        if letra in "aeiouAEIOU":
            contador += 1
    if contador > maior:
        maior = contador

lista = []
for p in palavras:
    contador = 0
    for letra in p:
        if letra in "aeiouAEIOU":
            contador += 1
    if contador == maior and p not in lista:
        lista.append(p)

print(f"Palavras com {maior} vogais:")
for i, palavra in enumerate(lista, start=1):
        print(f"{i}- {palavra}")