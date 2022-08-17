# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

# num = int(input('Digite um número: '))
# if (num % 2) == 0:
#     print('O número digitado é par!'.format(num))
# else:
#     print('O número digitado é ímpar!'.format(num))

número = int(input('Digite um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR.'.format(número))
else:
    print('O número {} é ímpar.'.format(número))

