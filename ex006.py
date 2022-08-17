# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# n = int(input('Digite um número: '))
# print('O dobro deste número é: {}'.format(n * 2))
# print('O triplo deste número é: {}'.format(n * 3))
# print('A raiz quadrada deste número é: {:.2f}'.format(n ** 0.5))

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}'.format(n, t, n, r))
