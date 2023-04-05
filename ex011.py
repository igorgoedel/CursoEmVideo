# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço , com 5% de descoto.
preço = float(input('Digite o preço :R$'))
desconto = preço - (preço * 0.5 / 100)
print('R${:.2f} com cinco por cento de desconto é R${:.2f}'.format(preço, desconto))
