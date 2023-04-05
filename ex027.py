#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
n = str(input('Digite seu nome completo: ')).strip()
nome =  n.split()
#Split é o comando responsavel por dividir o nome, separar cada nome do nome completo. Como exemplo de um print do codigo até aqui com a variavael nome.
print('Seu primerio nome é {}'.format(nome[0]))
#print('Seu ultimo nome é {}'.format(nome[3]))
#Esse codigo pode dar erro porque a caixa 3 pode não ter no proximo nome. Por isso foi colocado a funçao len, ela vai dizer quantos nome tem, portanto ela vai mostrar o nome na posiçao de nome menos 1.
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))