#exercicios de tratamento de exceção. slide do exercicios no teams no dia 21 de maio de 2025
#é para fazer cadastro do cliente (nome, sobrenome, rg, cfp, endereço, fone, idade)
#é para fazer cadastro da passagem (destino, origem, duração, valor passagem, desconto 5%)
#é para fazer cadastro avião (modelo, ano, horas do voo, cor, quantidade de passageiros)
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
            rg=input('Digite o RG: ')
            cpf=input('Digite o CPF: ')
            endereco=input('Digite o Endereço: ')
            cel=input('Digite o Celular: ')
            idade=int(input('Digite a Idade: '))
            cliente.append({
    'nome': nome,
    'sobrenome': sobrenome,
    'rg': rg,
    'cpf': cpf,
    'endereco': endereco,
    'celular': cel,
    'idade': idade})

        except ValueError as e:
            print(f"Erro ao cadastrar. Verifique os dados numéricos. Detalhes: {e}")

#dados passagens
    elif menu=='2': 
        try:
            destino=input('Digite o destino da passagem: ')
            origem=input('Digite a origem: ')
            duracao=input('Digite a duração do VOO: ')
            preco=float(input('Digite o valor da passagem: '))
            desc=0.05*preco
            preco_desc=0.95*preco
            passagem.append({
    'destino da passagem': destino,
    'origem da passagem': origem,
    'tempo de voo': duracao,
    'valor da passagem': preco,
    'desconto de 5%': desc,
    'valor da passagem com desconto': preco_desc})

        except ValueError as e:
            print(f"Erro ao cadastrar. Verifique os dados numéricos. Detalhes: {e}")

#dados avião
    elif menu=='3':
        try:
            modelo=input('Digite o modelo do avião: ')
            ano=int(input('Digite o ano do avião: '))
            tempovoo=(input('Digite quanto tempo de voo tem o avião: '))
            cor=input('Digite a cor do avião: ')
            numacentos=int(input('Digite quantos assentos tem o avião: '))
            aviao.append({
    'modelo do avião': modelo,
    'ano de fabricação': ano,
    'horas de voo': tempovoo,
    'a cor do avião': cor,
    'quantidade de assentos': numacentos})

        except ValueError as e:
            print(f"Erro ao cadastrar. Verifique os dados numéricos. Detalhes: {e}")

    #dados da tripulação:
    elif menu=='4':
        try:
            numtripulantes=int(input('Digite quantos tripulantes terá o avião nessa viagem: '))
        except ValueError:
            print('é preciso ser um numero')
            continue
        for i in range(numtripulantes):
            try:
                nomepiloto=input('Nome: ')
                funcao=input('Função: ')
                idadetrip=int(input('Idade: '))
                dataadimissao=input('Data de admissão: ')
                fone=int(input('Telefone de contato: '))
                tripulacao.append({
    'Nome ': nomepiloto,
    'Função': funcao,
    'Idade': idadetrip,
    'Data de admissão': dataadimissao,
    'telefone': fone})

            except ValueError as e:
                print(f"Erro ao cadastrar. Verifique os dados numéricos. Detalhes: {e}")
    
    #relatorio
    elif menu=='5':
        while True:
            menu1=input("Digite: \n1--para relatório cliente: \n2--para relatório da passagem: \n3--para relatório do avião: \n4--relatório da tripulação: \ndigite x para sair: ").lower()
            try:
                if menu1=='1':
                    for i, c in enumerate(cliente):
                        print(f"\nCliente {i+1}:")
                        for chave, valor in c.items():
                            print(f"{chave.capitalize()}: {valor}")

                elif menu1=='2':
                   for i, c in enumerate(passagem):
                        print(f"\nPassagens {i+1}:")
                        for chave, valor in c.items():
                            print(f"{chave.capitalize()}: {valor}")
                elif menu1=='3':
                    for i, c in enumerate(aviao):
                        print(f"\nAvião {i+1}:")
                        for chave, valor in c.items():
                            print(f"{chave.capitalize()}: {valor}")
                elif menu1=='4':
                    for i, c in enumerate(tripulacao):
                        print(f"\nTripulação {i+1}:")
                        for chave, valor in c.items():
                            print(f"{chave.capitalize()}: {valor}")
                elif menu1=='x':
                    print('Encerrando o programa...')
                    break
                else:
                    print('Opção inválida.')
            except ValueError as e:
                print(f"Erro ao cadastrar. Verifique os dados numéricos. Detalhes: {e}")
    elif menu == 'x':
        print('Encerrando o programa...')
        break
    else:
        print('Opção inválida.')




#acredito que consegui fazer, acho que ainda pode ser melhorado, mas a ajuda do gravena nas monitorias é que proporciono o termino do codigo, a parte do print dos relatorios fiz de uma forma que imprimia a lista e ficava muito ruim ai pedi ajuda a IA para ver se tinha outra forma de fazer ela me sugeriu fazer por dicionario depois da explicação de como se faz consegui alterar essa parte. 
#seria bom receber um feedback. se puder fico agradecido.

