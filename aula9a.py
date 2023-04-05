frase = 'Curso em Vídeo'
print(frase[3])
#Esse comando pega só a caixa '3' da variável frase, mas ele não pega exatamente a caixa três, mas sim a caixa 4, porque o contador de python começa a contar da caixa 0.

frase = 'Curso em Vídeo'
print(frase[3:13])
#Esse comando vai escrever os dados da caixa três até a caixa 13.

frase = 'Curso em Vídeo'
print(frase[3:])
#Esse comando como não especifica a ultima caixa depois dos dois pontos vai fazer o python ir até o final da frase.

frase = 'Cruso em Vídeo'
print(frase[1:15:2])
#Nesse comando depois do segundo dois pontos, vai fazer com que o contador escreva as coixas pulando elas de dois em dois.

frase = 'Curso em Vídeo'
print(frase[::2])
#Aqui ele vai pular de dois em dois a frase toda.

frase = 'Curos em Vídeo'
print(frase.count('o'))
#Nesse comando python vai imprimir com o contadro só as letras 'o'.

frase = ' Curso em Vídeo   '
print(len(frase.strip()))
#Aqui ele vai ler o comprimento da frase, quantas caixas ou letras a frase tem. O comando strip remove os espaços vazios no final e no começo das frases.

frase = 'Cruso em Vídeo Python'
print(frase.replace('Python', 'Android'))
#Esse comando replace ele troca a palavra python por androind, mas não altera permanentemente a string.

frase = 'Curso em Vídeo Python'
print('Curso' in frase)
#'In' me diz se tem ou não tem 'Curso' na variavel frase.

frase = 'Cruso em Vídeo Python'
print(frase.find('Vídeo'))
#find vai me mostrar a posiçao que está a palavra Vídeo dentro da variável frase.

frase = 'Curso em Vídeo'
print(frase.split())
#Esse comando vai deixar cada palavra da variável frase em lista.