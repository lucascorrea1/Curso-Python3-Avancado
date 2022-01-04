# positivos [12345678]
texto = 'Python s2'

print(texto[2])

#negativos -[987654321]

nova_string = texto[2:6]  # Inicia pegando o caractere 't' e termina no 'n'.
print(nova_string)

nova_string_exclusao = texto[:-2]  # Exclui os últimos dois caracteres.
print(nova_string_exclusao)

print(len(texto))  # conta a qnt. de caracteres da string.

#  Entender que as Strings possuem índices.

for letra in texto:
    print(letra)



