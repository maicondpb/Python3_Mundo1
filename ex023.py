# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex. Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

numero = int(input('Digite um número de 0 a 9999: '))
print('Analisando o número {}...'.format(numero))
unidade = (numero // 1) % 10
print('A unidade deste número é {}'.format(unidade))
dezena = (numero // 10) % 10
print('A dezena deste número é {}'.format(dezena))
centena = (numero // 100) % 10
print('A centena deste número é {}'.format(centena))
milhar = (numero // 1000) % 10
print('O milhar deste número é {}'.format(milhar))

# num = int(input('Informe um número: '))
# n = str(num)
# print('Analisando o número {}'.format(num))
# print('Unidade: {}'.format(n[3]))
# print('Dezena: {}'.format(n[2]))
# print('Centena: {}'.format(n[1]))
# print('Milhar: {}'.format(n[0]))
# daria erro se fizesse por exemplo do número 123

