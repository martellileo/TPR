arquivo = "arquivo.txt"
saida = "saida.txt"

with open(arquivo, 'r') as f:
    linhas = f.readlines()

palavras = []
linhas_numeradas = []
contagem = {}
resumo = {}

for i, linha in enumerate(linhas, start=1):
    linhas_numeradas.append(f"{i:04d} {linha.strip()}")

    palavras_linha = linha.strip().split()
    palavras.extend(palavras_linha)

    for palavra in palavras_linha:
        contagem[palavra] = contagem.get(palavra, 0) + 1
        resumo[len(palavra)] = resumo.get(len(palavra), 0) + 1

maior = max(palavras, key=len)
menor = min(palavras, key=len)

repetidas = {}
for palavra, qtd in contagem.items():
    if qtd > 1:
        repetidas[palavra] = qtd

with open(saida, 'w') as f:
    f.write("Linhas numeradas:\n")
    for linha in linhas_numeradas:
        f.write(linha + "\n")

    f.write(f"\nMaior palavra: {maior}\n")
    f.write(f"Menor palavra: {menor}\n")

    f.write("\nPalavras repetidas:\n")
    for p, c in repetidas.items():
        f.write(f"{p} => {c}\n")

    f.write("\nResumo:\n")
    for tamanho in sorted(resumo):
        f.write(f"Com {tamanho} letras = {resumo[tamanho]}\n")
