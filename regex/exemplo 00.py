import re

texto = "JOAO SILVA foi com MARIA SOUZA"
padrao = r'[A-Z]+'
pattern = re.compile(padrao)

print(re.findall(padrao, texto))
print(re.search(padrao, texto))
print(re.match(padrao, texto))


match = re.search(pattern, texto)
print(match.group())