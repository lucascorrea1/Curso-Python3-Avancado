nome = "Lucas Corrêa"
idade = 21
altura = 1.72
peso = 78.00
anoAtual = 2021
imc = (peso / (altura ** altura))

print(nome, 'tem', idade, 'anos,', altura, 'de altura e pesa', peso,'kg')
print('O IMC de', nome, 'é {:.2f}'.format(imc, prec=2))
print(nome, 'nasceu em', anoAtual - idade)