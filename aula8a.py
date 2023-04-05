#Mostradno a importanção da biblioteca math
import math
num = float(input('\033[1;33;40mDigite um número e eu digo a sua raiz: \033[m'))
raiz = math.sqrt(num)
print('\033[1;33;40ma raiz de {:.2f} é {:.2f}\033[m'.format(num, raiz))
#Outra forma de importar diretamente na funcionalidade que você quiser, control + espaço depois de escrever o nome da biblioteca, esse comando aponta os seus módulos as suas funcionalidades
from math import sqrt
num = int(input('\033[1;35;40mDigite um número e eu te mostrarei a sua raiz quadrada: \033[m'))
raiz = sqrt(num)
print('\033[1;35;40mA raiz de {} é {}\033[m'.format(num, raiz))
#Mostrando a biblioteca de emojis ela não é bull-in, não vem intalada com o python
import emoji
print(emoji.emojize("Olá, mundo!:earth_americas: "))