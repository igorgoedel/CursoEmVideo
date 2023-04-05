#Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar.
#num = int(input('Digite um número:'))
#if
#    print('Seu número escolhido foi {}, é um número é par.')
#else:
#    print('Seu número digitado foi {}, é um número impar.')
#Não  concegui fazer esse exercicio.
#Jeito do professor

numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é par!'.format(resultado))
else:
    print('O número {} é impar!'.format(resultado))