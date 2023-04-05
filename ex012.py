#Faça um algoritmo que leia o sálario de um funcionário e mostre e mostre seu novo sálario, com 15% de aumento.
salario = float(input('Digite o seu salário: R$'))
novo = salario + (salario*15/100)
print('Seu salário R${:.2f} com o aumento de 15% ficou {:.2f}'.format(salario, novo))