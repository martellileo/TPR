import re

texto = 'abc123def456ghi789'

padrao_nao_abc = re.findall(r'[^abc]', texto)
print('Caracteres que não são "a", "b" ou "c":', padrao_nao_abc)
