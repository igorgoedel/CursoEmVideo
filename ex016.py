#Faça um programa que leia o comprimento e o cateto oposto e do cateto adjasente de um triângulo retângulo, calcule e mostre o comprimento da hipoternusa.
co = float(input('Digite o número do cateto oposto:'))
ca = float(input('Digite o número do cateto adjacente:'))
hi = (co ** 2 + ca **2) ** (1/2)
print('A hipoternusa vai medir {:.2f}'.format(hi))
#Maneira feita sem importação
import math
co = float(input('Digite o número do cateto oposto:'))
ca = float(input('Digite o número do cateto adjacente:'))
hi = math.hypot(co, ca)
print('A hipoternusa vai medir {:.2f}'.format(hi))
#Tambem poderia importa somente o método hyport, e pra isso é só olhar o exercício passado.