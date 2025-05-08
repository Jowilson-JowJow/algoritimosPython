#fazer o sistema bancario foto da aula 
while True:
    lista_clientes=[]
    clientes=input('NOME: ')
    cpf=int(input('CPF: '))
    rg=int(input('RG: '))
    telefone=input('TELEFONE: ')
    agencia=input('AGENCIA: ')
    conta=input('CONTA: ')
    saldo=float(input('SALDO: '))
    lista_clientes.append(clientes)
    lista_clientes.append(cpf)
    lista_clientes.append(rg)
    lista_clientes.append(telefone)
    lista_clientes.append(agencia)
    lista_clientes.append(conta)
    lista_clientes.append(saldo)
    #lista_clientes.extend([clientes,cpf,rg,telefone,agencia,conta,saldo]) DESSA FORMA NÃO PRECISA FAZER TODOS OS APPENDS EM SEPARADOS
    print(lista_clientes)
    while True:
        x=(input('Digite:\n1--para ver saldo: \n2--para depositar: \n3--sacar: \n4--sair: '))
        if x=='1':
            print (lista_clientes[6])
        elif x=='2':
            deposito=int(input('Qual o valor a depositar: (R$) '))
            while deposito <=0:
                print('valor incorreto')
                deposito=int(input('Qual o valor a depositar: (R$) '))
            lista_clientes[6]=lista_clientes[6]+deposito
            print(lista_clientes[6])
        elif x=='3':
            saque=int(input("Digite o valor para saque: (R$) "))
            while saque <=0:
                print('valor incorreto')
                saque=int(input("Digite o valor para saque: (R$) "))
            if lista_clientes[6]<saque:  
                 print('proibido o saque.')
            else:
                lista_clientes[6]=lista_clientes[6]-saque
            print(lista_clientes[6])
        elif x=='4':
            break




    
