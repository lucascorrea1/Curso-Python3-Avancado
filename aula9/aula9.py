
nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

ano_atual = 2021
ano_nascimento = ano_atual - int(idade)

print()
print(f'{nome} tem {idade} anos.\n'
      f'{nome} nasceu em {ano_nascimento}.')

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))

print('Resultado da soma:', numero_1 + numero_2)