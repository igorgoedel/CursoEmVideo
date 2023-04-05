nome = str(input('Qual é o seu nome ?'))
if nome == 'Gustavo':
    print('Que nome legal você tem!')
else:
    print('Seu é muito bonito!')
print('Prazer {}!'.format(nome))
#Repare a indentação todas as condições escritas as esquerda elas vão ser escritas, já as que estão mais pra dentro podem ou não serem escritas.

nota = float(input('Digite a sua nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
resultado = (nota + nota2) / 2
print('Sua nota foi {}'.format(resultado))
if nota >= 6.0:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')