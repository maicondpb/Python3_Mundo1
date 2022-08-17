# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santo"

# cidade = str(input('Em que cidade você nasceu? ')).strip()
# cidade = cidade.upper()
# print(cidade)
# print('SANTO' in cidade)

cidade = str(input('Qual é a cidade que você nasceu? ')).strip()
cidade = cidade.upper()
print('Sua cidade começa com a palavra Santo? {}'.format(cidade[:5] == 'SANTO'))
