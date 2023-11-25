cont = 0
while True:
    usuario = str(input('nome de usuario:')).lower().strip()
    senha = int (input('senha:').strip())
    if usuario == 'davi' and senha == 1234:
        print('saldo:1.500')
        break
    if usuario != 'davi' or senha != 1234:
        print('senha ou usuario invalidos!')
        cont = cont + 1
    if cont >= 3 :
        print('conta bloqueada')
