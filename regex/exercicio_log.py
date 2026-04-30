import re

padrao = r'connection authorized|disconnection'

with open("dados.txt", "r") as f:
    for linha in f:
        if re.search(padrao, linha):
            print(linha.strip())