#Crie um algortimo que leia um número e mostre seu dobro, seu triplo, e a sua raiz quadrada.
#n = input('Digite um número: ')
#n1 = n * 2
#n2 = n * 3
#n3 = n ** (1/2)
#print('o dobro de {} é {} e o triplo é {} e a sua raiz quadrada é {}.'.format(n, n1, n2, n3))

n = int(input('Digite um número:' ))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro do número {} vale {}.'.format(n, d))
print('O triplo de {} vale {}. \nE a raiz quadrada de {} vale {:.2f}.'.format(n, t, n, r))

#Outra forma de fazer o mesmo código.
n = int(input('Digite um número: '))
print('O dobro de {} é {}.\nO triplo de {} é {}.\nA raiz quadrada de {} é {:.2f}.'.format(n, (n*2), n, (n*3), n, (n ** (1/2))))