#Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem.
#Cobrando R$0,50 por km para viagens até  200 km e R$ 0,45 para viagens mais longas.
dis = int(input('Digite a distância da viagem: '))
cin = dis * 0.50
qua = dis * 0.45
if dis <= 200:
    print('A sua viajem custará {} reais.'.format(cin))
else:
    print('A sua viajem custrá {} reais.'.format(qua))

#Jeito do professor.
distancia = float(input('Qual é a distancia da sua viajem?'))
print('Você está prestes a começar uma viajem de {}km'.format(distancia))
if distancia <= 200:
    preso = distancia * 0.50
else:
    preso = distancia * 0.45
print('O preço da sua passagem será R${:.2f}'.format(preso))

#Outra forma de fazer o mesmo exercico.
distancia = float(input('Qual é a distância da sua viajem?'))
print('Você está prestes a começar uma viajem de {}km'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço será de R${:.2f}'.format(preco))