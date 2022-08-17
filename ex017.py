# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um trinângulo retângulo, calcule e mostre o comprimento da hipotenusa.

# co = float(input('Digite o comprimento do cateto oposto: '))
# ca = float(input('Digite o comprimento do cateto adjacente: '))
#
# hipotenusa = (ca ** 2 + co ** 2) ** (1/2)
#
# print('O valor da hipotenusa é: {:.2f}'.format(hipotenusa))

from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('O valor da hipotenusa é: {:.2f}'.format(hi))
