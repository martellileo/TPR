import re

texto = 'A idade dele é 25 anos e o número de telefone é (123) 456-7890.'

pattern = re.compile(r'\d+')

numeros = re.findall(pattern, texto)

print(numeros)
