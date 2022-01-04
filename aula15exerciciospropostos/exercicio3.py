primeiro_nome = input('Digite o seu primeiro nome: ')

#  mostra quantidade de caracteres do nome digitado
print('O nome digitado possui', len(primeiro_nome), 'letras.')

try:
    if len(primeiro_nome) <= 4:
        print('Seu nome é curto.')
    elif 5 <= len(primeiro_nome) <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande. ')
except:
    'Erro! Você não digitou um nome corretamente! Dica: Utilize somente letras. '

