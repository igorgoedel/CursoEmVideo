#Escreva um programa que leia um valor em metros e o exiba em valores convertido em centímetros e milímetros.
metro = float(input('Digite a quantidade de metro: '))
centimetros = metro * 100
milimetros = metro * 1000
print('{} m convertidos em centimetros são {} cm, e em milímetros mm são {} .'.format(metro, centimetros, milimetros,))