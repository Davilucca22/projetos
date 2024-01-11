import datetime
from time import sleep
print('----------ALISTAMENTO MILITAR-----------')
print('digite [parar] para encerrar o programa.')

while True:
    nome = str(input('digite seu nome:'))
    print(f'ola {nome}')
    print('digite seu sexo')
    entrada = str(input('entrada:').lower()).strip()

    if  entrada == 'masculino':
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
        
    elif entrada == 'feminino':
        print('o alistamento nao é obrigatório para mulheres')
    elif entrada != 'masculino' and entrada != 'feminino' and entrada != 'parar':
        print('\033[0;31mvalor invalido!'+'\033[m')
    if entrada == 'parar':
        print('encerrando programa...')
        sleep(3)
        break
print('programa encerrado!')
