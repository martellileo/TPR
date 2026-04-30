import re

'''

Correspondência de caracteres específicos:
[abc]: Corresponde a qualquer caractere dentro dos colchetes (neste exemplo, a, b ou c).
[^abc]: Corresponde a qualquer caractere que não esteja dentro dos colchetes (neste exemplo, qualquer caractere exceto a, b e c).
[a-z]: Corresponde a qualquer caractere minúsculo de a a z.
[A-Z]: Corresponde a qualquer caractere maiúsculo de A a Z.
[0-9]: Corresponde a qualquer dígito de 0 a 9.
Correspondência de quantificadores:
*: Corresponde a zero ou mais vezes.
+: Corresponde a uma ou mais vezes.
?: Corresponde a zero ou uma vez.
{n}: Corresponde exatamente n vezes.
{n,}: Corresponde pelo menos n vezes.
{n,m}: Corresponde de n a m vezes.
Correspondência de posições:
^: Corresponde ao início da string.
$: Corresponde ao final da string.
\b: Corresponde a uma palavra (borda de palavra).
Correspondência de caracteres especiais:
\d: Corresponde a qualquer dígito de 0 a 9.
\w: Corresponde a qualquer caractere alfanumérico (letras, números e sublinhados).
\s: Corresponde a qualquer caractere de espaço em branco (espaço, tabulação, quebra de 

'''

pattern = re.compile(r'\d+')
texto = 'A idade dele é 25 anos.'

match = re.search(pattern, texto)

if match:
    print('Número encontrado:', match.group())
else:
    print('Número não encontrado.')


pattern = re.compile(r'\(\d{2}\) \d{5}-\d{4}')
texto = "Este é o telefone (18) 99812-9384 vai ser retirado texto"

match = re.search(pattern, texto)
print(match.group())