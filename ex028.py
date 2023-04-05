#Escreva um programa que faça o computador "pensar"em um numero inteiro entre 0 e 5.
#E peça para o usuario tentar descobrir qual foi o numereo escolhido pelo computador.
#O programa deverá escrever  na tela se o usuario venceu ou perdeu.
num = int(input('Escolha um número de 0 a 5: '))
if num == '3':
    print('Seu escolha está correta!, Você escolheu o número {}.'.format(num))
else:
    print('Seu resposta está incorreta!, você escolheu o numero {}.'.format(num))

#Jeito do professor
from random import randint
computador = randint (0,5)#Comando que faz o computador 'Pensar'.
jogador = int(input('Vou pensar em um número entre 0 e 5, tente advinhar.. '))
print('Processando...')
sleep(3)#Comando que faz esperar por 3 segundos antes da resposta.
if jogador == computador:
    print('Parabéns você acertou!')
else:
    print('Você não acertou!')