# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar; Considere US$ 1.00 = R$ 3.27

r = float(input('Digite quanto dinheiro você tem na carteira: R$ '))
d = r / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(r, d))
