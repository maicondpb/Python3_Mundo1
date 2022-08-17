# Condições
# Simples e Compostas

carro.siga()
carro.esquerda()
carro.siga()
carro.direita()
carro.siga()
carro.direita()
carro.siga()
carro.esquerda()
carro.siga()
carro.pare()

comandos sequenciais de cima pra baixo, esquerda pra direita (início ao fim)

carro.siga()

se carro.esquerda()     |   senão
    carro.siga()               carro.siga()
    carro.direita()            carro.esquerda()
    carro.siga()               carro.siga()
    carro.direita()            carro.esquerda()
    carro.esquerda()           carro.siga()
    carro.siga()
    carro.direita()
    carro.siga()

carro.pare()

-------

se carro.esquerda()
    bloco_V_
senão
    bloco_F_

if carro.esquerda():
    bloco True
else:
    bloco False



tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')


tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <=3 else 'carro velho')
print('__FIM__')