print('-'*35)
print('PROGRAMA SUBTRAÇAO')
print('-'*35)

cont = int (input('quantas contas deseja fazer?:'))

for c in range(0,cont):
    print('-'*35)
    print(f'conta {c+1}:')
    n1 = int(input('digite um numero:'))
    n2 = int(input('digite outro numero:'))
    print(f'{n1} - {n2} = {n1-n2}')
    print('-'*35)

print('fim')
