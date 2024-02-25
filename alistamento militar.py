import datetime ;from time import sleep
print('----------ALISTAMENTO MILITAR-----------')
while True:
    print('-'*30)
    print(f'ola,o que voce deseja fazer?\n[1]consultar o tempo que falta ou excedeu para o alistamento\n[2]parar o programa')
    entrada = int (input('entrada:').lower())
    print('-'*30)

    if entrada == 1:
        sexo = str(input('qual o seu sexo?[m/f]:').lower()).strip()[0]
        print('-'*30)

        if  sexo == 'm':
            ano_nascimento = int(input('ano de nascimento:'))
            ano_atual = datetime.datetime.today().year
            idade = ano_atual - ano_nascimento
            print(f'voce tem {idade} anos')

            if idade < 18:
                tempo = 18 - idade
                print(f'\033[0;32mfaltam {tempo} anos para voce se alistar'+'\033[m')

            elif idade > 18:
                tempo = idade - 18
                print(f'\033[0;31mvoce deveria ter se alistado há {tempo} anos atrás'+'\033[m')

            elif idade == 18:
                print('\033[0;34mvoce deve se alistar este ano'+'\033[m')
            
        elif sexo == 'f':
            print('o alistamento nao é obrigatório para mulheres')

    elif entrada == 2:
            print('encerrando programa...')
            sleep(3)
            break
    else:
        print('\033[0;31mvalor invalido!'+'\033[m')

print('programa encerrado!')