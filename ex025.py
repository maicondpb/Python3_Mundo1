# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = str(input('Qual é seu nome completo? ')).strip()
nome = nome.upper()
print('Seu nome tem silva? {}'.format('SILVA' in nome))
