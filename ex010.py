#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua ára e a quantia de tinta necessária para pinta-la , sabendo que cada litro de tinta pinta uma área de 2m**2.
larg = float(input('Digite a largura da parede: '))
cump = float(input('Digite o cumprimento da parede: '))
area = larg * cump
print('Sua parede {}x{}, tem a área de {}m.'.format(larg, cump, area))
tinta = area / 2
print('Você vai precisar de {}l de tinta para pintar sua parede.'.format(tinta))
#Eu não tinha conceguido fazer esse exercicio.