numb = int(input('digite um numero:'))
cont = 0

print(f'numeros impares ate {numb}:')
for c in range(0,numb+1):
    if c % 2 == 1:
        print(c,end='-> ')
        cont += 1

print('fim!')
print('-'*50)