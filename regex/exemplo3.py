import re

lista = ''' 
   Vilson 111.111.111-11
   Joao   222.222.222-22
   Pedro  333.333.333-33 '''

pattern = re.compile(r'\d{3}\.\d{3}.\d{3}\-\d{2}')
cpfs = re.findall(pattern, lista)
print(cpfs)