# While em Python
# Utilizado para realizar ações enquanto uma condição for verdadeira.
# Requisitos: Entender condições e operadores

x = 0 # coluna
while x < 10:
    y = 0  # linha
    while y < 5:
        print(f'X vale {x},{y}')
        y += 1
    x += 1 # x = x + 1


while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')


    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número')

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *
    if operador == '+':
        print(f'Resultado:', num_1 + num_2)
    elif operador == '-':
        print(f'Resultado:', num_1 - num_2)
    elif operador == '/':
        print(f'Resultado:', num_1 / num_2)
    elif operador == '*':
        print(f'Resultado:', num_1 * num_2)
    else:
        print('Operador Inválido!')

    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break
