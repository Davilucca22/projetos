
while True:
    nome = str(input('nome do contato:'))
    telefone = int(input('numero de telefone:'))

    esc = int(input('[1]adiconar contatos\n[2]ver contatos\n[3]sair\n:'))
    
    if esc == 1:
       nome = str(input('nome do contato:'))
       telefone = int(input('numero de telefone:')) 
    elif esc == 2:
        print(nome)
        print(telefone)
    else:
        break
