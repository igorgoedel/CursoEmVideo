#Crie um programa que leia que quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
#Concidere USS 1 = RS 3.27.
cart = float(input('Quanto tens na carteira ? '))
uss = cart / 3.27
print('Seu dinheiro convertido em dólares é {:.2f}.'.format(uss))