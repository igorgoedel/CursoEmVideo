#style 0 padrão , 1 negrito , 4 sublinhado , 7 inverte as cores de fundo e da letra
#30 branco,31 vermelho, 32 verde, 33 amarelo, 34 azul fraco , 35 lilas , 36 azul esverdeado, 37 cinza
#back40,41,42,43,44,45,46,47

print('\033[31mOlá mundo!')
print('\033[31;43mOlá mundo!')
print('\033[1;31;43mOlá mundo!')
print('\033[1;31;43mOlá mundo!\033[m')

nome = 'Igor'
print('Olá, Prazer em te conhcer {}{}{}!!'.format('\033[4;34m', nome, '\033[m'))