from Cliente import Cliente
import os

while True:
    print("Loja on line JowTCG")
    print("*"*30)
    print("Selecione uma opção:")
    opcao=input("\t1 - Cadastrar\n\t2 - listar\n\t3 - Excluir\n\t4 - Atualisar\n\t0 - sair\n")
    result = 0
    if opcao =="0":
        break

    if opcao =="1":
        os.system("cls")
        while True:
            opcao1 = input("\t1 - Cadastrar Cliente\n\t0 - Sair\n")
            if opcao1=="0":
                break

            if opcao1 =="1":
                os.system("cls")
                cli = Cliente()
                cli.nome = input("Digite o nome do cliente: ")
                cli.email = input("Digite o email do Cliente: ")
                cli.fone = input("Digite o Telefone do cliente: ")
                result = cli.cadastrar_cliente()
            if result == True:
                print("Cadastrado com Sucesso!!!")

    if opcao=="2":
        os.system("cls")
        while True:
            opcao1 = input("\t1 - Listar Cliente\n\t0 - Sair\n")

            if opcao1 == "0":
                break

            if opcao1 == "1":
                os.system("cls")
                cli = Cliente()
                result = cli.buscar_cliente()
                for cliente in result:
                    print(f"ID: {cliente[0]} | Nome: {cliente[1]}  | Email: {cliente[2]} | Fone: {cliente[3]}")

    if opcao =="3":
        os.system("cls")
        while True:
            opcao1 = input("\t1 - Excluir Cliente\n\t0 - Sair")

            if opcao1 == "0":
                break

            if opcao1 == "1":
                os.system("cls")
                cli = Cliente()
                result = cli.buscar_cliente()
                for cliente in result:
                    print(f"ID: {cliente[0]} | Nome: {cliente[1]}  | Email: {cliente[2]} | Fone: {cliente[3]}")

                id_excluir = int(input("Digite o id que deseja excluir: "))
                result = cli.excluir_cliente(id_excluir)
                if result == True:
                    print("Cliente excluido com sucesso!!!")

    if opcao=="4":
        os.system
        while True:
            opcao1 = input("\t1 - Atualizar Cliente\n\t0 - Sair\n")
           
            if opcao1=="0":
                break
        
            if opcao1=="1":
                cli = Cliente()
                result = cli.buscar_cliente()
                for cliente in result:
                    print(f"ID: {cliente[0]} | Nome: {cliente[1]}  | Email: {cliente[2]} | Fone: {cliente[3]}")

                id_atualizar =int(input("Digite o ID do cliente que deseja atualizar: ") )
                result = list(cli.buscar_por_id_cliente(id_atualizar))
                result[1]=input("Digite o novo nome do cliente: ")
                result[2] = input ("Digite o novo email do cliente: ")
                result[3] = input("Digite o novo telefone: ")
                atualizacao = cli.atualizar_cliente(tuple(result))
                if atualizacao == True:
                    print("Cliente atualizado com sucesso!!!")
        