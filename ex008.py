#Faça um programa que leia um número inteiro qualquer e o mostre na tela a sua tabuada.
print('-' * 12)
num = int(input('Digite um numero de 1 a 10: '))
print('{} x 1 = {:2}'.format(num, (num*1)))
print('{} x 2 = {:2}'.format(num, (num*2)))
print('-'* 12)
#{:2} é usado para alinhas os numeros colocando eles em duas caixas