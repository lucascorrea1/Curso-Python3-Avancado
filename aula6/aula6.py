nome = "Lucas Corrêa"
idade = 21
altura = 1.72
e_maior = idade > 18
peso = 79
imc = peso / altura ** altura

print(nome, 'tem ', idade, ' anos de idade e seu IMC é {:.2f}'.format(imc, prec=2))