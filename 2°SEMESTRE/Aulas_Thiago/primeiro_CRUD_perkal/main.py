from Cliente import Cliente
from Mecanico import Mecanico

while True:
    print("SysPerkal")
    print("*"*30)
    print("Selecione um opção")
    opcao=input("\t1 - Cadastrar\n\t2 - listar\n\t3 - Excluir\n\t4 - Atualisar\n\t0 - sair\n")

    if opcao =="0":
        break

    if opcao == "1":
        
        while True:
            opcao1 = input("\t1 - Cadastrar Cliente\n\t2 - Cadastrar Mecanico\n\t0 - Sair\n ")
            
            if opcao1 == "0":
                break

            if opcao1 == "1":
                cli = Cliente()
                cli.nome = input("Digite o nome do cliente: ")
                cli.cpf = input("Digite o CPF: ")
                cli.fone = input("Digite o fone: ")
                cli.cidade = input("Digite o Cidade: ")
                result = cli.cadastrar_cli()
            
            if result == True:
                print("Cadastrado com sucesso!!!")

            if opcao1 =="2":
                mec = Mecanico()
                mec.nome = input("Digite o nome do Mecânico: ")
                mec.cpf = input("Digite o CPF: ")
                mec.cod_mec = input("Digite o Código do Mecânico: ")
                mec.fone = input("Digite o Telefone: ")
                result = mec.cadastrar_mec()
            
            if result == True:
                print("Cadastrado com sucesso!!!")

    if opcao == "2":
        while True:
            opcao1 = input("\t1 - Listar Cliente\n\t2 - Listar Mecanico\n\t0 - Sair\n ")
            
            if opcao1 == "0":
                break

            if opcao1 =="1":
                cli = Cliente()
                result = cli.buscar_cli() # reotrna lista de tulpla
                for cliente in result:
                    print(f'ID: {cliente[0]} | NOME: {cliente[1]} | CPF: {cliente[2]} | FONE: {cliente[3]} |CIDADE: {cliente[4]}')

            if opcao1 =="2":
                mec = Mecanico()
                result = mec.buscar_mec() # reotrna lista de tulpla
                for cad_mecanico in result:
                    print(f'ID: {cad_mecanico[0]} | NOME: {cad_mecanico[1]} | CPF: {cad_mecanico[2]} | Codigo Mecanico: {cad_mecanico[3]} |Fone: {cad_mecanico[4]}')

    
    if opcao == "3":
        while True:
            
            opcao1 = input("\t1 - Excluir Cliente\n\t2 - Excluir Mecanico\n\t0 - Sair\n ")
            
            if opcao1 == "0":
                break

            if opcao1 =="1":
                cli = Cliente()
                result = cli.buscar_cli() # reotrna lista de tulpla
                for cliente in result:
                    print(f'ID: {cliente[0]} | NOME: {cliente[1]} | CPF: {cliente[2]} | FONE: {cliente[3]} |CIDADE: {cliente[4]}')
        
                id_excluir = int(input("Digite o id que deseja excluir"))
                result = cli.excluir_cli(id_excluir)
                if result == True:
                    print("Excluido(a) com sucesso!!!")

            if opcao1 =="2":
                mec = Mecanico()
                result = mec.buscar_mec() # reotrna lista de tulpla
                for cod_mecanico in result:
                    print(f'ID: {cod_mecanico[0]} | NOME: {cod_mecanico[1]} | CPF: {cod_mecanico[2]} | Codigo Mecânico: {cod_mecanico[3]} |Fone: {cod_mecanico[4]}')
        
                id_excluir = int(input("Digite o id que deseja excluir"))
                result = mec.excluir_mec(id_excluir)
                if result == True:
                    print("Excluido(a) com sucesso!!!")


    elif opcao =="4":
        while True:
            opcao1 = input("\t1 - Atualizar Cliente\n\t2 - Atualizar Mecanico\n\t0 - Sair\n ")
            
            if opcao1 == "0":
                break

            if opcao1 =="1":
                cli = Cliente()
                result = cli.buscar_cli() # reotrna lista de tulpla
                for cliente in result:
                    print(f'ID: {cliente[0]} | NOME: {cliente[1]} | CPF: {cliente[2]} | FONE: {cliente[3]} |CIDADE: {cliente[4]}')

                id_atualizar = int(input("Digite o ID do Cliente que deseja atualizae: "))
                result = list(cli.buscar_por_id_cli(id_atualizar))
                result[1] = input("Digite o novo Nome: ")
                result[2] = input("Digite o novo CPF: ")
                result[3] = input("Digite o novo FONE: ")
                result[4] = input("Digite a nova CIDADE: ")
                atualizacao = cli.atualizar_cli(tuple(result))
                if atualizacao == True:
                    print("CLiente atualizado com sucesso!!!")

            if opcao1 =="2":
                mec = Mecanico()
                result = mec.buscar_mec() # reotrna lista de tulpla
                for cod_mecanico in result:
                    print(f'ID: {cod_mecanico[0]} | NOME: {cod_mecanico[1]} | CPF: {cod_mecanico[2]} | Codigo Mecânico: {cod_mecanico[3]} |Fone: {cod_mecanico[4]}')

                id_atualizar = int(input("Digite o ID do Cliente que deseja atualizae: "))
                result = list(mec.buscar_por_id_mec(id_atualizar))
                result[1] = input("Digite o novo Nome: ")
                result[2] = input("Digite o novo CPF: ")
                result[3] = input("Digite o novo Codigo Meca^nico: ")
                result[4] = input("Digite a nova Fone: ")
                atualizacao = mec.atualizar_mec(tuple(result))
                if atualizacao == True:
                    print("CLiente atualizado com sucesso!!!")