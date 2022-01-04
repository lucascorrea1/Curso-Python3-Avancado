numero = input('Digite um número inteiro: ')

try:
    numero = int(numero)

    if numero % 2 == 0:
        print('É Par.')
    else:
        print('É Impar.')
except:
    print('Não é um número inteiro.')
