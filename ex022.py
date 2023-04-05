#Crie um programa que leia que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúscolas e minúscolas.
#Quantas letras ao todo (sem se conciderar os espaços).
#Quantas letras tem no primerio nome.

nome = str(input('Digite o seu nome completo:')).strip()
#A função de strip aqui é eliminar os espaços em branco no final e no começo do input.
print('Seu nome com letras maiúscolas é {}.'.format(nome.upper()))
print('Seu nome com letras minúscolas é {}.'.format(nome.lower()))
print('Seu nome ao todo tem {} letras.'.format(len(nome) - nome.count(' ')))
#Aqui a função ' - nome.count(' ')' ela elimina a contagem dos espaços em branco do meio da frase.
#print('Seu primeiro nome tem {} letras'.format(nome.find('   ')))
#esse print de cima mostra um jeito de mostrar o primeiro nome.
separa = nome.split()
print(separa)
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))