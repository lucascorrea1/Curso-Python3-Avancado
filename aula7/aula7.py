nome = "Lucas Corrêa"
idade = 21
altura = 1.72
e_maior = idade > 18
peso = 79
imc = peso / altura ** altura

print(nome, 'tem ', idade, ' anos de idade e seu IMC é', imc)

#  com formatação de duas casas decimais
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos e seu imc é {}'.format(nome, idade, imc))