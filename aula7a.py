nome = input('\033[1;33;44mQual é o seu nome ? \033[m')
print('Prazer em te conhecer {:20}!'.format( nome))
#O Código escreveu a variável nome em vinte espaços.

nome = input('\033[1;30;44mQual é o seu nome ? \033[m')
print('Prazer em te conhcer {:>20}!'.format(nome))
#Agora o código está alinhando a variável nome dentro dos 20 espaços estabelecidos dentro do colchetes, para a direita.

nome = input('\033[1;30;45mQual é o seu nome ?\033[m')
print('\033[1;30;45mPrazer em te conhcer {:<20}!\033[m'.format(nome))
#Agora a variável nome está alinhada a esquerda.

nome = input('Qual é o seu nome ?')
print('Prazer em te conhecer {}{}{}!!'.format('\033[4;34;40m', nome, '\033[m'))
#Agora a variável nome está no meio.


