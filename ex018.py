# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# import math
# angulo = float(input('Digite o ângulo que você deseja: '))
# print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, math.sin(math.radians(angulo))))
# print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, math.cos(math.radians(angulo))))
# print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, math.tan(math.radians(angulo))))


from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, sin(radians(angulo))))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cos(radians(angulo))))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tan(radians(angulo))))