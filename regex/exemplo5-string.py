import re

texto = 'A batata tem 123 calorias.'

padrao_intervalo = re.findall(r'[A-Za-f]', texto)
print('Caracteres dentro do intervalo:', padrao_intervalo)
