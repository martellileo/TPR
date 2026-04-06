arquivo = "arquivo3.txt"

with open(arquivo, 'r') as f:
    linhas = f.readlines()

for i, linha in enumerate(linhas, start=1):
    palavras = linha.strip().split()
    ordem = sorted(palavras, key=len)
    saida = "|" + "|".join(ordem) + "|"
    print(f"linha {i:02d} - {saida}")