# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
area = l * a
print('Sua parede tem a dimensão de {} x {} e sua área da parede é de: {}m²'.format(l, a, area))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(area / 2))

