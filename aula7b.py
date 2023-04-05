n1 = (input('\033[1;31;40mDigite um número: \033[m'))
n2 = (input('\033[1;31;40mDigite outro número: \033[m'))
print('A soma vale {}.'.format('\033[1;31m', n1 + n2, '\033[m'))
# A soma feita só com format.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1+n2
d = n1/n2
m = n1*n2
di = n1//n2
e = n1**n2
print('O resoltado da soma é {}, o resultado da divisão é {:.3f} e o resultado da multiplicação é {}.'.format(s, d, m), end=' ')
print('A Divisão inteira é {} e a potenciação é {}.'.format(di, e))
#O resultado da variável (d) é delimitado o número de carácteres dentro do colchetes {:.3f}.
#No final da linha 13 o comando (end='') junta as duas linhas.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1+n2
d = n1/n2
m = n1*n2
di = n1//n2
e = n1**n2
print('O resoltado da soma é {}, \n O resultado da divisão é {:.3f} \n E o resultado da multiplicação é {}.'.format(s, d, m))
print('A Divisão inteira é {} \n E a potenciação é {}.'.format(di, e))
#(\n) divide as frases imprimidas.