# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais o aumento é de 15%.

salario = float(input('Digite o valor do salário: R$'))
if salario > 1250:
    print('O salário terá um aumento de 10%, ficando no valor de R${:.2f}'.format(salario + (salario * 10 / 100)))
else:
    print('O salário terá um aumento de 15%, ficando no valor de R${:.2f}'.format(salario + (salario * 15 / 100)))
