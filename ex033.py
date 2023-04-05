#Faça um programa que leia três numeros e mostre qual é o maior e qual é o menor.
#num1 = int(input('Digite um número: '))
#num2 = int(input('Digite outro número: '))
#num3 = int(input('Digite mais um outro número: '))
#num4 = num2 > num3
#num5 = num2
#if num1 > num4:
#    print('Número mais alto é {}'.format(num1))
#if num1 < num
#Jeito do professor.

a = int(input('Digite um valor:'))
b = int(input('Digite outro valor: '))
c = int(input('Digite mais um valor: '))
#Verificando quem é o menor.
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando o maior.
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor verificado foi {}'.format(menor))
print('O maior valor verificado foi {}'.format(maior))