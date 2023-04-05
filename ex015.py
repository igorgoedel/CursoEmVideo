# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite o número: 6.127 e o númerp 6.127 tem a parte intera 6.

from math import trunc
num = float(input('Digite um número:'))
print('A parte interia do número que você digitou é {}.'.format(num, trunc(num)))
# importou a biblioteca a função trunc da biblioteca math, função que tira os pontos fluatuantes.
#Quando é importada a biblioteca inteira com 'import math', é preciso colocar a referencia de math antes do trunc no comando format, escreve math.trunc().

num = float(input('Digite um número:'))
print('O número que você digitou é {} e a parte dele inteira é {}.'.format(num, int(num)))
#Outra forma de fazre o mesmo código.