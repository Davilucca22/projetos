senha = 2005
x = int(input('digite a senha:'))
if x != senha:
    for c in range (1,7):
     x = int(input('tente novamente:'))
     if x == senha:
        print('acesso liberado!')
        break
     if c == 3:
        novasenha = int(input('defina uma nova senha:'))
        senha = novasenha
else:
   print('acesso liberado')
