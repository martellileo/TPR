import re

texto = 'Python é uma Linguagem de Programação'

padrao_maiusculas = re.findall(r'[A-Z]', texto)
print('Letras maiúsculas:', padrao_maiusculas)

padrao_minusculas = re.findall(r'[a-z]', texto)
print('Letras minúsculas:', padrao_minusculas)
