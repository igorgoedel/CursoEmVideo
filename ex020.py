#O mesmo professor do desafio anterior quer sortear a ordem de apresentação  de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mpstre a ordem sorteada.
from random import shuffle
n1 = str(input('Digite primeiro aluno: '))
n2 = str(input('Digite segundo aluno: '))
n3 = str(input('Digite terceiro aluno: '))
n4 = str(input('Digite quarto aluno: '))
lista = [n1, n2, n3 ,n4]
shuffle(lista)
print('A ordem de execução será ')
print(lista)
#Essa é a funcionalidade do modulo random.