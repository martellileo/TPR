import re

texto = 'O número de 888 telefone é (123) 456-7890.'

padrao_digitos = re.findall(r'[0-9]', texto)
print('Dígitos encontrados:', padrao_digitos)
