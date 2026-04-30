import re

texto = 'A batata tem 123 calorias. c2'
padrao_palavras_c = re.findall(r'\b[cC]\w+', texto)

print('Caracteres dentro do intervalo:', padrao_palavras_c)


