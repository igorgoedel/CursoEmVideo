#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite.
vel = int(input('Digite a velocidade do carro: '))
mul = vel - 80
multa = mul *7
if vel >= 81:
    print('Você ultrapassou o limite de velocidade, Sua multa será {} reais.'.format(multa))
else:
    print('Você não ultrapassou o limite de velocidade.')

#Jeito do professor
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULATDO! Você excedeu o limite de velocidade permitido que é de 80 km/h!')
    multa = (velocidade - 80) * 7
    print('Você precisa pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
#Repare que le não usou o comando 'else' isso se chama de condição simples.