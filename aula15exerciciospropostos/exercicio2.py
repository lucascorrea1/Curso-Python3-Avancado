perguntaHora = input('Digite a hora atual: ')
perguntaHora = int(perguntaHora)

try:
    if 0 <= perguntaHora <= 11:
        print('Bom dia')
    elif 12 <= perguntaHora <= 17:
        print('Boa tarde')
    else:
        print('Boa noite!')
except:
    print('Error! Você não informou a hora corretamente.')
