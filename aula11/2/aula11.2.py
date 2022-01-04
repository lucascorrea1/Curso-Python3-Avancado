# Operadores Lógicos
# and, or, not
# in, not in

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'lucas'
senha_bd = '123456'

if(usuario_bd == usuario and senha_bd == senha):
    print('Você está logado no sistema')
else:
    print('O usuário ou a senha estão inválidos.')