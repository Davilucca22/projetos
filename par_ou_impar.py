from random import randint

while True:
    entrada = int(input('vamos jogar par ou impar!\ndigite um numero:'))

    pc = randint(0,10)

    numb = entrada + pc

    opc = str(input('par ou impar?:'))

    print('-'*30)
    if opc == 'par' and numb % 2 == 0:
        print('voce venceu!')

    elif opc == 'impar' and numb % 2 != 0:
        print('voce venceu!')

    else:
        print('voce perdeu!')
    print('-'*30)

    print(f'pc jogou:{pc}')
    print('-'*30)

    esc = str(input('deseja jogar novamente?[S/N]:').upper())[0]

    if esc == 'N':
        break

print('programa encerrado')