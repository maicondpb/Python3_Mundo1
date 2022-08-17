# import math
# num = int(input('Digite um número: '))
# raiz = math.sqrt(num)
# print('A raíz de {} é igual a {:.2f}'.format(num, raiz))

from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raíz de {} é igual a {:.2f}'.format(num, floor(raiz)))