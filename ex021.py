#Faça um programa em python que abra e produzza um arquivo em mp3.
#Eunào tenho uma música no meu pc, e nem vou baixar, mas só é preciso copiar e colar no pasta do projeto 'CursoEmVideo'
#Ai vai abrir um documento junto com os exercícios.
#Existem várias bibliotecas usadas em python e diversos modulos feitos por outros programadores, mas aqui nesse curso foi usado o paygame
#Nessa versão de python não tem a biblioteca paygame, mas é só escrever import paygame e clicar na lampada vermelha que aparecer e pedir pra instalar
import paygame
paygame.init()
paygame.mixer.music.load('ex021.mp3')
paygame.mixer.music.play()
paygame.event.wait()
#ex01.mp3 é o arquivo com a musica colada no começo do programa.