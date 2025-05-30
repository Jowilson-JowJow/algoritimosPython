#exercicios de tratamento de exceção. slide do exercicios no teams no dia 21 de maio de 2025
#é para fazer cadastro do cliente (nome, sobrenome, rg, cfp, endereço, fone, idade)
#é para fazer cadastro da passagem (destino, origem, duração, valor passagem, desconto 5%)
#é para fazer cadastro avião (modelo, ano, hoaras do voo, cor, quantidade de passageiros)
#é para fazer cadastro tripulação (nome, descrição cargo, idade, data de adimissão, fone)
# O Algoritmo deve ter a opção de cadastrar, imprimir relatórios e encerrar.
#Utilize todas as técnicas possíveis, while, for, try, etc...


cliente=[]
passagem=[]
aviao=[]
tripulacao=[]
#cadastro cliente
while True:
    menu=input("Digite: \n1--para cadastrar cliente: \n2--para dados da passagem: \n3--para dados do avião: \n4--dados da tripulação: \n5--imprimir relatórios: \ndigite x para sair: ").lower()
    if menu=='1':
        try:
            nome=input('Digite o nome: ')
            sobrenome=input('Digite o sobrenome: ')
            rg=int(input('Digite o RG: '))
            cpf=int(input('Digite o CPF: '))
            endereco=input('Digite o Endereço: ')
            cel=int(input('Digite o cel: '))
            idade=int(input('Digite a Idade: '))
            # cliente.extend([nome,sobrenome,rg,cpf,endereco,cel,idade])
            cliente.append({
    'nome': nome,
    'sobrenome': sobrenome,
    'rg': rg,
    'cpf': cpf,
    'endereco': endereco,
    'cel': cel,
    'idade': idade
})

        except:
            print('Dados Incorretos')

#dados passagens
    elif menu=='2': 
        try:
            destino=input('Digite o destino da passagem: ')
            origem=input('Digite a origem: ')
            duracao=input('Digite a duração do VOO: ')
            preco=float(input('Digite o valor da passagem: '))
            desc=0.95*preco
            # passagem.extend([destino,origem,duracao,preco,desc])
            cliente.append({
    'nome': nome,
    'sobrenome': sobrenome,
    'rg': rg,
    'cpf': cpf,
    'endereco': endereco,
    'cel': cel,
    'idade': idade
})

        except:
            print('Dados Incorretos')

#dados avião
    elif menu=='3':
        try:
            modelo=input('Digite o modelo do avião: ')
            ano=int(input('Digite o ano do avião: '))
            tempovoo=(input('Digite quanto tempo de voo tem o avião: '))
            cor=input('Digite a cor do avião: ')
            numacentos=int(input('Digite quantos assentos tem o avião: '))
            # aviao.extend([modelo,ano,tempovoo,cor,numacentos])
            cliente.append({
    'nome': nome,
    'sobrenome': sobrenome,
    'rg': rg,
    'cpf': cpf,
    'endereco': endereco,
    'cel': cel,
    'idade': idade
})

        except:
            print('Dados Incorretos')

    #dados da tripulação:
    elif menu=='4':
        try:
            numtripulantes=int(input('Digite quantos tripulantes terá o avião nessa viagem: '))
        except:
            print('é preciso ser um numero')
        for i in range(numtripulantes):
            try:
                nomepiloto=input('Digite o nome do piloto: ')
                funcao=input('Digite a função: ')
                idadetrip=int(input('Digite a idade do tripulante: '))
                dataadimissao=input('Digite a data de adimissão: ')
                fone=int(input('Digite o telefone de contato: '))
                # tripulacao.extend([nomepiloto, funcao, idadetrip, dataadimissao, fone])
                cliente.append({
    'nome': nome,
    'sobrenome': sobrenome,
    'rg': rg,
    'cpf': cpf,
    'endereco': endereco,
    'cel': cel,
    'idade': idade
})

            except:
                print('Dados Incorretos')
    
    #relatorio
    elif menu=='5':
        while True:
            menu1=input("Digite: \n1--para telatório cliente: \n2--para relatório da passagem: \n3--para relatório do avião: \n4--relatório da tripulação: \ndigite x para sair: ").lower()
            try:
                if menu1=='1':
                    for i, c in enumerate(cliente):
                        print(f"\nCliente {i+1}:")
                        for chave, valor in c.items():
                            print(f"{chave.capitalize()}: {valor}")

                elif menu1=='2':
                   # print(f' Informações da passagem: {passagem}')
                elif menu1=='3':
                    #print(f' Os dados do avição são: {aviao}')
                elif menu1=='4':
                    #print(f'os dados da tripulação são: {tripulacao}')
                elif menu1=='x':
                    #print('Encerrando o programa...')
                    break
                else:
                    print('Opção inválida.')
            except:
                print('Dados digitados de forma incorretos')
    elif menu == 'x':
        print('Encerrando o programa...')
        break
    else:
        print('Opção inválida.')






