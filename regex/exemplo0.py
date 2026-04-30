texto = 'A idade é 25 anos'

linha=''
for x in texto:
    if x in '0123456789':
       linha+=x
print(linha)