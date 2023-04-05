#Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antesessor.
#n = input('Digíte um número: ')
#print('Seu antessesor é {}, e seu sucessor é {}.'.format(n-1, n+1))
#Travei não sábia oque fazer.

n = int(input('Digite um número: '))
ant = n - 1
suc = n + 1
print('Analisando o número {} o seu antessesor é {} e o seu sucessor é {}.'.format(n, ant, suc))

#Outra maneira de fazer o mesmo código.
n = int(input('Digite um número: '))
print('Análisando o número {} seu antessesor é {} e o seu sucessor é {}.'.format(n, (n-1), (n+1)))