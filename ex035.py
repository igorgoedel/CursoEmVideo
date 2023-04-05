#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo.
print('-=' * 20)
print('Analisando Triângulo')
print('-=' * 20)
r1 = float(input('Primeiro seguomento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar triângulo.')
else:
    print('Os seguimtnos acima não podem formar triângulo.')