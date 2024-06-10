# CONDIÇÃO
import random
# from random import randint
from time import sleep
print('-=-' * 20)
print('ADIVINHE O NUMERO QUE ESTOU PENSANDO....=)')
print('-=-' *20)
maquina = (random.randint(0, 5))
# n1 = randint(0, 5) .........Fazer um sorteio entre 0 a 5.
jogador = int(input('Digite um numero de 0 á 5:  '))
print('Processando...')
sleep(1)
if maquina == jogador:
    print('Parabéns, você acertou o numero...')
else:
    print('Que pena, você errou!! =(')
print('*' * 50)
print('O meu numero escolhido foi {}' .format(maquina))
print('*' * 50)