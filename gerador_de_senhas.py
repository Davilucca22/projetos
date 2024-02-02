import random

minusculas = 'abcdefghijklmnopqrstuvwxyz'

maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

numeros = '0123456789'

simbolos = '@#$%&*'

senha = random.choices((minusculas)+(maiusculas)+(numeros)+(simbolos))

print(senha)