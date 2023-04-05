#Desenvolva um programa que mostre as duas notas de um aluno, calcule e mostre a sua média.
nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))
nota3 = nota1 + nota2
nota4 = nota3 // 2
if nota3 >= 6:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')
#Não errei, mas o professor fez diferente

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
n = (n1 + n2) / 2
print('A media entre {:.1f} e {:.1f} é {:.1f}!'.format(n1, n2, n))