# Escreve um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# n = float(input('Digite o valor em metros: '))
# print('O valor convertido em centímetros é: {}'.format(n * 100))
# print('O valor convertido em milímetros é: {}'.format(n * 1000))

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
dc = medida * 0.1
hc = medida * 0.01
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))
print('A medida de {}m corresponde a {:.0f}dm, {:.0f}dc e {}hc'.format(medida, dm, dc, hc))


