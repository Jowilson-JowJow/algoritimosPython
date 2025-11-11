from Cliente import Cliente

while True:
    print("SysPerkal")
    print("*"*30)
    print("Selecione um opção")
    opcao=input("\t1 - Cadastrar\n\t2 - listar Cliente\n\t3 - Excluir Cliente\n\t4 - Atualisar\n\t0 - sair\n")

    if opcao =="0":
        break

    if opcao == "1":
        cli = Cliente()
        cli.nome = input("Digite o nome do cliente: ")
        cli.cpf = input("Digite o CPF: ")
        cli.fone = input("Digite o fone: ")
        cli.cidade = input("Digite o Cidade: ")
        result = cli.cadastrar()
        if result == True:
            print("Cadastrado com sucesso!!!")

    if opcao == "2":
        cli = Cliente()
        result = cli.buscar() # reotrna lista de tulpla
        for cliente in result:
            print(f'ID: {cliente[0]} | NOME: {cliente[1]} | CPF: {cliente[2]} | FONE: {cliente[3]} |CIDADE: {cliente[4]}')

    
    if opcao == "3":
        cli = Cliente()
        result = cli.buscar() # reotrna lista de tulpla
        for cliente in result:
            print(f'ID: {cliente[0]} | NOME: {cliente[1]} | CPF: {cliente[2]} | FONE: {cliente[3]} |CIDADE: {cliente[4]}')
        
        id_excluir = int(input("Digite o id que deseja excluir"))
        result = cli.excluir(id_excluir)
        if result == True:
            print("Excluido(a) com sucesso!!!")

    elif opcao =="4":
        cli = Cliente()
        result = cli.buscar() # reotrna lista de tulpla
        for cliente in result:
            print(f'ID: {cliente[0]} | NOME: {cliente[1]} | CPF: {cliente[2]} | FONE: {cliente[3]} |CIDADE: {cliente[4]}')

        id_atualizar = int(input("Digite o ID do Cliente que deseja atualizae: "))
        result = list(cli.buscar_por_id(id_atualizar))
        result[1] = input("Digite o novo Nome: ")
        result[2] = input("Digite o novo CPF: ")
        result[3] = input("Digite o novo FONE: ")
        result[4] = input("Digite a nova CIDADE: ")
        atualizacao = cli.atualizar(tuple(result))
        if atualizacao == True:
            print("CLiente atualizado com sucesso!!!")
