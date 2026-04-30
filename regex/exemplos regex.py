import re

# ============================================
# CORRESPONDÊNCIA DE CARACTERES ESPECÍFICOS
# ============================================

# [abc] - Corresponde a qualquer caractere dentro dos colchetes (a, b ou c)
r'[abc]'  # Em "abacate" retorna: ['a', 'b', 'a', 'a']

# [^abc] - Corresponde a qualquer caractere que NÃO esteja dentro dos colchetes
r'[^abc]'  # Em "abacate" retorna: ['c', 't', 'e']

# [a-z] - Corresponde a qualquer caractere minúsculo de a a z
r'[a-z]'  # Em "Olá123" retorna: ['l', 'á']

# [A-Z] - Corresponde a qualquer caractere maiúsculo de A a Z
r'[A-Z]'  # Em "Olá Mundo" retorna: ['O', 'M']

# [0-9] - Corresponde a qualquer dígito de 0 a 9
r'[0-9]'  # Em "Casa123" retorna: ['1', '2', '3']

# ============================================
# CORRESPONDÊNCIA DE QUANTIFICADORES
# ============================================

# * - Corresponde a zero ou mais vezes
r'ab*c'  # Em "ac abc abbc" retorna: ['ac', 'abc', 'abbc']

# + - Corresponde a uma ou mais vezes
r'ab+c'  # Em "ac abc abbc" retorna: ['abc', 'abbc']

# ? - Corresponde a zero ou uma vez
r'ab?c'  # Em "ac abc abbc" retorna: ['ac', 'abc']

# {n} - Corresponde exatamente n vezes
r'a{3}'  # Em "aa aaa aaaa" retorna: ['aaa', 'aaa']

# {n,} - Corresponde pelo menos n vezes
r'a{2,}'  # Em "a aa aaa aaaa" retorna: ['aa', 'aaa', 'aaaa']

# {n,m} - Corresponde de n a m vezes
r'a{2,3}'  # Em "a aa aaa aaaa" retorna: ['aa', 'aaa', 'aaa']

# ============================================
# CORRESPONDÊNCIA DE POSIÇÕES
# ============================================

# ^ - Corresponde ao início da string
r'^Olá'  # Em "Olá mundo" retorna: ['Olá']
r'^Olá'  # Em "Diga Olá" retorna: []

# $ - Corresponde ao final da string
r'mundo$'  # Em "Olá mundo" retorna: ['mundo']
r'mundo$'  # Em "mundo está aqui" retorna: []

# \b - Corresponde a uma borda de palavra
r'\bPython\b'  # Em "Python é legal, iPython também" retorna: ['Python']

# ============================================
# CORRESPONDÊNCIA DE CARACTERES ESPECIAIS
# ============================================

# \d - Corresponde a qualquer dígito de 0 a 9 (equivalente a [0-9])
r'\d'  # Em "Ano 2024" retorna: ['2', '0', '2', '4']

# \w - Corresponde a qualquer caractere alfanumérico (letras, números e sublinhados)
r'\w'  # Em "Olá_123 mundo!" retorna: ['O', 'l', 'á', '_', '1', '2', '3', 'm', 'u', 'n', 'd', 'o']

# \s - Corresponde a qualquer caractere de espaço em branco (espaço, tabulação, quebra de linha)
r'\s'  # Em "Olá mundo\n!" retorna: [' ', '\n']

# ============================================
# EXEMPLOS PRÁTICOS COMPLETOS
# ============================================

# Validar email simples
r'\w+@\w+\.\w+'  # Em "user@email.com" retorna: ['user@email.com']

# Extrair números de telefone (formato: 99999-9999)
r'\d{5}-\d{4}'  # Em "Ligue: 12345-6789" retorna: ['12345-6789']

# Encontrar palavras que começam com maiúscula
r'\b[A-Z]\w+'  # Em "Python é Legal" retorna: ['Python', 'Legal']

# Extrair CEP (formato: 99999-999)
r'\d{5}-\d{3}'  # Em "CEP: 12345-678" retorna: ['12345-678']

# Encontrar URLs
r'https?://\w+\.\w+'  # Em "Visite http://site.com" retorna: ['http://site.com']
