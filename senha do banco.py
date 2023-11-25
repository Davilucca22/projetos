padrao = (1234)
for c in range (0,3):
    senha = int (input('digite sua senha para ver saldo em conta\n:'))
    if senha != padrao :
        print('senha invalida!')
if senha == padrao:
    print('saldo disponivel:1500.00')
        