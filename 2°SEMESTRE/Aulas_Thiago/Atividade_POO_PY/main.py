from Cliente import Cliente
from Vendedores import Vendedores
from Cards import Cards
from Vendas import Vendas
import os

while True:
    print("\n\n\n\n\nLoja on line JowTCG")
    print("*"*30)
    print("Selecione uma opção:")
    opcao=input("\t1 - Cadastrar\n\t2 - listar\n\t3 - Excluir\n\t4 - Atualisar\n\t0 - sair\n")
    result = 0
    if opcao =="0":
        break

    if opcao =="1":
        os.system("cls")
        while True:
            opcao1 = input("\t1 - Cadastrar Cliente\n\t2 - Cadastrar Vendedor\n\t3 - Cadastrar Cards\n\t4 - Cadastrar Vendas\n\t0 - Sair\n")
            if opcao1=="0":
                break

            if opcao1 =="1":
                os.system("cls")
                cli = Cliente()
                cli.nome = input("Digite o nome do cliente: ")
                cli.email = input("Digite o email do Cliente: ")
                cli.fone = input("Digite o Telefone do cliente: ")
                result = cli.cadastrar_cliente()
            # if result == True:
            #     print("Cadastrado com Sucesso!!!")
           
            if opcao1 =="2":
                os.system("cls")
                vend = Vendedores()
                vend.nome = input("Digite o nome do vendedor: ")
                vend.cod_vendedor = input("Digite o codigo do vendedor: ")
                vend.fone = input("Digite o Telefone do vendedor: ")
                result = vend.cadastrar_vendedor()
            # if result == True:
            #     print("Cadastrado com Sucesso!!!")
            
            if opcao1 =="3":
                os.system("cls")
                card = Cards()
                card.nome_card = input("Digite o nome do card: ")
                card.preco_card = input("Digite o preço do card: ")
                card.qtde_card = input("Digite a quantidade do card: ")
                card.raridade_card = input("Digite a raridade do card: ")
                card.edicao_card = input("Digite a edição do card: ")
                result = card.cadastrar_card()
            # if result == True:
            #     print("Cadastrado com Sucesso!!!")
            
            if opcao1 =="4":
                os.system("cls")
                venda = Vendas()
                venda.nome_card = input("Digite o nome do card: ")
                venda.qtde_venda = input("Digite a quantidade de card vendidos: ")
                venda.valor_total = input("Digite o valor total da venda: ")
                result = venda.cadastrar_venda()
            if result == True:
                print("Cadastrado com Sucesso!!!")

    if opcao=="2":
        os.system("cls")
        while True:
            opcao1 = input("\t1 - Listar Cliente\n\t2 - Listar Vendedor\n\t3 - Listar Card\n\t4 - Listar Vendas\n\t0 - Sair\n")

            if opcao1 == "0":
                break

            if opcao1 == "1":
                os.system("cls")
                cli = Cliente()
                result = cli.buscar_cliente()
                for cliente in result:
                    print(f"ID: {cliente[0]} | Nome: {cliente[1]}  | Email: {cliente[2]} | Fone: {cliente[3]}")
           
            if opcao1 == "2":
                os.system("cls")
                vend = Vendedores()
                result = vend.buscar_vendedor()
                for vendedor in result:
                    print(f"ID: {vendedor[0]} | Nome: {vendedor[1]}  | Codigo Vendedor: {vendedor[2]} | Fone: {vendedor[3]}")
            
            if opcao1 == "3":
                os.system("cls")
                card = Cards()
                result = card.buscar_card()
                for card in result:
                    print(f"ID: {card[0]} | Nome do card: {card[1]}  | preço do card: {card[2]} | Quantidade do card: {card[3]} | Raridade do card: {card[4]} | Edicão do card: {card[5]}")
            
            if opcao1 == "4":
                os.system("cls")
                venda = Vendas()
                result = venda.buscar_venda()
                for item in result:
                    print(f"ID: {item[0]} | Nome do card: {item[1]}  | Quantidade vendida: {item[2]} | Valor total da venda: {item[3]}")

    if opcao =="3":
        os.system("cls")
        while True:
            opcao1 = input("\t1 - Excluir Cliente\n\t2 - Excluir Vendedor\n\t3 - Excluir Cards\n\t0 - Sair\n")

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
           
            if opcao1 == "2":
                os.system("cls")
                vend = Vendedores()
                result = vend.buscar_vendedor()
                for vendedor in result:
                    print(f"ID: {vendedor[0]} | Nome: {vendedor[1]}  | Codigo Vendedor: {vendedor[2]} | Fone: {vendedor[3]}")

                id_excluir = int(input("Digite o id que deseja excluir: "))
                result = vend.excluir_vendedor(id_excluir)
                if result == True:
                    print("vendedor excluido com sucesso!!!")
           
            if opcao1 == "3":
                os.system("cls")
                card = Cards()
                result = card.buscar_card()
                for card in result:
                    print(f"ID: {card[0]} | Nome do card: {card[1]}  | preço do card: {card[2]} | Quantidade do card: {card[3]} | Raridade do card: {card[4]} | Edicão do card: {card[5]}")

                id_excluir = int(input("Digite o id que deseja excluir: "))
                result = card.excluir_card(id_excluir)
                if result == True:
                    print("Card excluido com sucesso!!!")
           
            if opcao1 == "4":
                os.system("cls")
                venda = Vendas()
                result = venda.buscar_venda()
                for item in result:
                    print(f"ID: {item[0]} | Nome do card: {item[1]}  | Quantidade vendida: {item[2]} | Valor total da venda: {item[3]}")

                id_excluir = int(input("Digite o id que deseja excluir: "))
                result = venda.excluir_venda(id_excluir)
                if result == True:
                    print("Venda excluido com sucesso!!!")

    if opcao=="4":
        os.system("cls")
        while True:
            opcao1 = input("\t1 - Atualizar Cliente\n\t2 - Atualizar Vendedor\n\t3 - Atualizar Card\n\t4 - Atualizar Venda\n\t0 - Sair\n")
           
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
            
            if opcao1=="2":
                vend = Vendedores()
                result = vend.buscar_vendedor()
                for vendedor in result:
                    print(f"ID: {vendedor[0]} | Nome: {vendedor[1]}  | Codigo Vendedor: {vendedor[2]} | Fone: {vendedor[3]}")

                id_atualizar =int(input("Digite o ID do vendedor que deseja atualizar: ") )
                result = list(vend.buscar_por_id_vendedor(id_atualizar))
                result[1]=input("Digite o novo nome do vendedor: ")
                result[2] = input ("Digite o novo codigo do vendedor: ")
                result[3] = input("Digite o novo telefone: ")
                atualizacao = vend.atualizar_vendedor(tuple(result))
                if atualizacao == True:
                    print("Vendedor atualizado com sucesso!!!")
           
            if opcao1=="3":
                os.system("cls")
                card = Cards()
                result = card.buscar_card()
                for card in result:
                    print(f"ID: {card[0]} | Nome do card: {card[1]}  | preço do card: {card[2]} | Quantidade do card: {card[3]} | Raridade do card: {card[4]} | Edicão do card: {card[5]}")

                id_atualizar =int(input("Digite o ID do card que deseja atualizar: ") )
                result = list(card.buscar_por_id_card(id_atualizar))
                result[1]=input("Digite o novo nome do card: ")
                result[2] = input ("Digite o novo preço do card: ")
                result[3] = input("Digite a nova quantidade do card: ")
                result[4] = input("Digite a nova raridade do card: ")
                result[5] = input("Digite a nova edição do card: ")
                atualizacao = card.atualizar_card(tuple(result))
                if atualizacao == True:
                    print("Card atualizado com sucesso!!!")
        
            if opcao1=="4":
                os.system("cls")
                venda = Vendas()
                result = venda.buscar_venda()
                for item in result:
                    print(f"ID: {item[0]} | Nome do card: {item[1]}  | Quantidade vendida: {item[2]} | Valor total da venda: {item[3]}")

                id_atualizar =input("Digite o ID da venda que deseja atualizar: ")
                result = list(venda.buscar_por_id_venda(id_atualizar))
                result[1]=input("Digite o novo nome do card: ")
                result[2] = input ("Digite a nova quantidade de cards vendido: ")
                result[3] = input("Digite o novo valor total: ")
                atualizacao = venda.atualizar_venda(tuple(result))
                if atualizacao == True:
                    print("Venda atualizado com sucesso!!!")
        