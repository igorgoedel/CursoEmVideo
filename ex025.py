#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.fomart(nome[:5] == 'Silva'))

#Outra forma de fazer a mesmo código.
nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('Silva' in nome))