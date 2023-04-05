#Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.
#n1 = input('Digite algo: ')
#print(type n1)
#print(n1 issubclass)
#Não soube fazer o exercício.
a = input('Digete algo: ')
print('O tipo primitivo desse valor é,',type(a))
print('Só tem espaços ? ', a.isspace())
print('É número ? ',a.isnumeric())
print('É alfabetico ? ', a.isalpha())
print('É alfanumérico ?', a.isalnum())
print('está em maiúscula ?', a.isupper())
print('Está em minúscula ?', a.islower())
print('Está capitalizada ?', a.istitle())