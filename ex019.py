#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
import random
n1 = str(input('Digite primeiro aluno: '))
n2 = str(input('Digite segundo aluno: '))
n3 = str(input('Digite terceiro aluno: '))
n4 = str(input('Digite quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno sorteado foi {}'.format(escolhido))
#Essa é a utilidade do módulo random