import re

texto = """
1. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
2. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
3. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
4. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
5. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
6. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
7. Phasellus lacinia id arcu sit amet malesuada.
8. Vestibulum eu velit et risus placerat fringilla.
9. Nullam lacinia magna quis posuere rutrum.
10. Integer fermentum nunc id massa condimentum, in hendrerit dolor pulvinar.
11. Quisque euismod justo in augue laoreet, sed vestibulum nunc sollicitudin.
12. Fusce euismod velit at tempor cursus.
13. Morbi fermentum libero a justo bibendum dignissim.
14. Vivamus nec felis a justo consequat commodo.
15. Donec ac massa nec tortor fringilla elementum.
16. Mauris eu risus sed quam pretium maximus.
17. Etiam commodo lorem id odio mattis, sit amet convallis tortor aliquet.
18. Suspendisse auctor nisi a felis tincidunt, eu fringilla dui ultricies.
19. Aenean ac sapien ut sapien lobortis euismod.
20. Cras at arcu vel nisi dictum placerat.
21. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;
22. Proin vel nunc quis felis varius sagittis.
23. Curabitur at justo in tortor commodo imperdiet.
24. Nam ut sapien non sapien lobortis fermentum.
25. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
26. Fusce ultricies magna a ligula interdum, nec fringilla enim rutrum.
27. Integer posuere magna ut est ultrices, at fringilla mauris dignissim.
28. Aliquam auctor orci in sapien dictum, ut aliquet ipsum fermentum.
29. Maecenas sed nunc sed libero rutrum varius.
30. Quisque gravida velit sit amet mauris consequat, id varius justo viverra.
"""

padrao1 = r'Lorem ipsum'  # Corresponde à frase "Lorem ipsum"
padrao2 = r'et dolore'  # Corresponde à frase "et dolore"
padrao3 = r'[A-Z]\w+'  # Corresponde a palavras começando com letra maiúscula
padrao4 = r'\d+'  # Corresponde a sequências de dígitos
padrao5 = r'\ba\w+\b'  # Corresponde a palavras que começam com 'a'

print('Padrão 1:', re.findall(padrao1, texto))
print('Padrão 2:', re.findall(padrao2, texto))
print('Padrão 3:', re.findall(padrao3, texto))
print('Padrão 4:', re.findall(padrao4, texto))
print('Padrão 5:', re.findall(padrao5, texto))
