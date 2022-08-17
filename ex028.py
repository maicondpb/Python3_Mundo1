# Escreve um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep

# num = random.randint(0, 5) # Faz o computador "pensar"
# chute = int(input('Digite um número entre 0 e 5 e descubra se acertou o número escolhido: ')) # Jogador tenta adivinhar
# if chute == num:
#     print('Você acertou!')
# else:
#     print('Você errou! O número escolhido era {}'.format(num))


computador = random.randint(0, 5) # Faz o computador 'pensar'
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))