# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

# n = float(input('Digite um valor: '))
# print('O valor digitado foi {} e sua porção inteira é {}'.format(n, int(n)))

from math import trunc
n = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(n, trunc(n)))

