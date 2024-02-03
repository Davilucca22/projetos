import random

minusculas = 'abcdefghijklmnopqrstuvwxyz'

maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

numeros = '0123456789'

simbolos = '@#$%&*'

num = int(input('quantos digitos sua senha deve ter?:'))

for c in range (0,num):
    senha = random.choice((minusculas)+(maiusculas)+(numeros)+(simbolos))
    print(senha,end='')