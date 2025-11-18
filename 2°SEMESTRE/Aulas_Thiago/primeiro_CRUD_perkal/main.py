from Cliente import Cliente
from Mecanico import Mecanico
from Pecas import Pecas
from Carros import Carros
import os
while True:
    print("SysPerkal")
    print("*"*30)
    print("Selecione uma opção:")
    opcao=input("\t1 - Cadastrar\n\t2 - listar\n\t3 - Excluir\n\t4 - Atualisar\n\t0 - sair\n")
    result=0
    if opcao =="0":
        break
    
    if opcao == "1":
        os.system("cls")
        while True:
            opcao1 = input("\t1 - Cadastrar Cliente\n\t2 - Cadastrar Mecanico\n\t3 - Cadastro Peças\n\t4 - Cadastro Carros\n\t0 - Sair\n ")
            
            if opcao1 == "0":
                break

            if opcao1 == "1":
                os.system("cls")
                cli = Cliente()
                cli.nome = input("Digite o nome do cliente: ")
                cli.cpf = input("Digite o CPF: ")
                cli.fone = input("Digite o fone: ")
                cli.cidade = input("Digite o Cidade: ")
                result = cli.cadastrar_cli()
            
            if result==True:
               print("Cadastrado com sucesso!!!")

            if opcao1 =="2":
                os.system("cls")
                mec = Mecanico()
                mec.nome = input("Digite o nome do Mecânico: ")
                mec.cpf = input("Digite o CPF: ")
                mec.cod_mec = input("Digite o Código do Mecânico: ")
                mec.fone = input("Digite o Telefone: ")
                result = mec.cadastrar_mec()
            
            if result==True:
               print("Cadastrado com sucesso!!!")

            if opcao1 =="3":
                os.system("cls")
                peca = Pecas()
                peca.nome_peca = input("Digite o nome da Peça: ")
                peca.preco = input("Digite o preço da peça: ")
                peca.qtde_peca = input("Digite a quantidade de peça: ")
                result = peca.cadastrar_peca()
            
            if result== True:
               print("Cadastrado com sucesso!!!")
           
            
            if opcao1 =="4":
                os.system("cls")
                car = Carros()
                car.nome_car = input("Digite o nome do carro: ")
                car.placa_car = input("Digite a placa do carro: ")
                car.estado_placa = input("Digite o estado da placa do carro: ")
                car.chassi_car = input("Digite o chassi do carro: ")
                result = car.cadastrar_car()
             
            
            if result==True:
                print("Cadastrado com sucesso!!!")

    if opcao == "2":
        os.system("cls")
        while True:
            opcao1 = input("\t1 - Listar Cliente\n\t2 - Listar Mecânico\n\t3 - Listar Peças\n\t4 - Listar Carro\n\t0 - Sair\n ")
            
            if opcao1 == "0":
                break

            if opcao1 =="1":
                os.system("cls")
                cli = Cliente()
                result = cli.buscar_cli() # reotrna lista de tulpla
                for cliente in result:
                    print(f'ID: {cliente[0]} | NOME: {cliente[1]} | CPF: {cliente[2]} | FONE: {cliente[3]} |CIDADE: {cliente[4]}')

            if opcao1 =="2":
                os.system("cls")
                mec = Mecanico()
                result = mec.buscar_mec() # reotrna lista de tulpla
                for cad_mecanico in result:
                    print(f'ID: {cad_mecanico[0]} | NOME: {cad_mecanico[1]} | CPF: {cad_mecanico[2]} | Codigo Mecanico: {cad_mecanico[3]} |Fone: {cad_mecanico[4]}')
            
            if opcao1 =="3":
                os.system("cls")
                peca = Pecas()
                result = peca.buscar_peca() # reotrna lista de tulpla
                for pecas in result:
                    print(f'ID: {pecas[0]} | NOME_PEÇAS: {pecas[1]} | PREÇO: {pecas[2]} | QTDE_PEÇAS: {pecas[3]}')

            if opcao1 =="4":
                os.system("cls")
                car = Carros()
                result = car.buscar_car() # reotrna lista de tulpla
                for carros in result:
                    print(f'ID: {carros[0]} | NOME_CAR: {carros[1]} | PLACA_CAR: {carros[2]} | ESTADO_PLACA: {carros[3]} |CHASSI_CAR: {carros[4]}')

    
    if opcao == "3":
        os.system("cls")
        while True:
            
            opcao1 = input("\t1 - Excluir Cliente\n\t2 - Excluir Mecanico\n\t3 - Excluir Peça\n\t4 - Excluir Carro\n\t0 - Sair\n ")
            
            if opcao1 == "0":
                break

            if opcao1 =="1":
                os.system("cls")
                cli = Cliente()
                result = cli.buscar_cli() # reotrna lista de tulpla
                for cliente in result:
                    print(f'ID: {cliente[0]} | NOME: {cliente[1]} | CPF: {cliente[2]} | FONE: {cliente[3]} |CIDADE: {cliente[4]}')
        
                id_excluir = int(input("Digite o id que deseja excluir"))
                result = cli.excluir_cli(id_excluir)
                if result == True:
                    print("Excluido(a) com sucesso!!!")

            if opcao1 =="2":
                os.system("cls")
                mec = Mecanico()
                result = mec.buscar_mec() # reotrna lista de tulpla
                for cod_mecanico in result:
                    print(f'ID: {cod_mecanico[0]} | NOME: {cod_mecanico[1]} | CPF: {cod_mecanico[2]} | Codigo Mecânico: {cod_mecanico[3]} |Fone: {cod_mecanico[4]}')
        
                id_excluir = int(input("Digite o id que deseja excluir"))
                result = mec.excluir_mec(id_excluir)
                if result == True:
                    print("Excluido(a) com sucesso!!!")

            if opcao1 =="3":
                os.system("cls")
                peca = Pecas()
                result = peca.buscar_peca() # reotrna lista de tulpla
                for pecas in result:
                    print(f'ID: {pecas[0]} | NOME_PEÇAS: {pecas[1]} | PREÇO: {pecas[2]} | QTDE_PEÇAS: {pecas[3]}')
        
                id_excluir = int(input("Digite o id que deseja excluir"))
                result = peca.excluir_peca(id_excluir)
                if result == True:
                    print("Excluido(a) com sucesso!!!")

            if opcao1 =="4":
                os.system("cls")
                car = Carros()
                result = car.buscar_car() # reotrna lista de tulpla
                for carros in result:
                    print(f'ID: {carros[0]} | NOME_CAR: {carros[1]} | PLACA_CAR: {carros[2]} | ESTADO_PLACA: {carros[3]} |CHASSI_car: {carros[4]}')
        
                id_excluir = int(input("Digite o id que deseja excluir"))
                result = car.excluir_car(id_excluir)
                if result == True:
                    print("Excluido(a) com sucesso!!!")


    elif opcao =="4":
        os.system("cls")
        while True:
            opcao1 = input("\t1 - Atualizar Cliente\n\t2 - Atualizar Mecanico\n\t3 - Atualizar Peças\n\t4 - Atualizar Carro\n\t0 - Sair\n ")
            
            if opcao1 == "0":
                break

            if opcao1 =="1":
                os.system("cls")
                cli = Cliente()
                result = cli.buscar_cli()
                for cliente in result:
                    print(f'ID: {cliente[0]} | NOME: {cliente[1]} | CPF: {cliente[2]} | FONE: {cliente[3]} |CIDADE: {cliente[4]}')

                id_atualizar = int(input("Digite o ID do Cliente que deseja atualizar: "))
                result = list(cli.buscar_por_id_cli(id_atualizar))
                result[1] = input("Digite o novo Nome: ")
                result[2] = input("Digite o novo CPF: ")
                result[3] = input("Digite o novo FONE: ")
                result[4] = input("Digite a nova CIDADE: ")
                atualizacao = cli.atualizar_cli(tuple(result))
                if atualizacao == True:
                    print("CLiente atualizado com sucesso!!!")

            if opcao1 =="2":
                os.system("cls")
                mec = Mecanico()
                result = mec.buscar_mec()
                for cod_mecanico in result:
                    print(f'ID: {cod_mecanico[0]} | NOME: {cod_mecanico[1]} | CPF: {cod_mecanico[2]} | Codigo Mecânico: {cod_mecanico[3]} |Fone: {cod_mecanico[4]}')

                id_atualizar = int(input("Digite o ID do Cliente que deseja atualizar: "))
                result = list(mec.buscar_por_id_mec(id_atualizar))
                result[1] = input("Digite o novo Nome: ")
                result[2] = input("Digite o novo CPF: ")
                result[3] = input("Digite o novo Codigo Mecânico: ")
                result[4] = input("Digite a nova Fone: ")
                atualizacao = mec.atualizar_mec(tuple(result))
                if atualizacao == True:
                    print("Mecânico atualizado com sucesso!!!")

            if opcao1 =="3":
                os.system("cls")
                peca = Pecas()
                result = peca.buscar_peca()
                for pecas in result:
                    print(f'ID: {pecas[0]} | NOME_PEÇAS: {pecas[1]} | PREÇO: {pecas[2]} | QTDE_PEÇAS: {pecas[3]}')

                id_atualizar = int(input("Digite o ID da Peça que deseja atualizar: "))
                result = list(peca.buscar_por_id_peca(id_atualizar))
                result[1] = input("Digite o novo Nome da peça: ")
                result[2] = input("Digite o novo preço da peça: ")
                result[3] = input("Digite a nova quantidade de peças: ")
                atualizacao = peca.atualizar_peca(tuple(result))
                if atualizacao == True:
                    print("Peça atualizado com sucesso!!!")

            if opcao1 =="4":
                os.system("cls")
                car = Carros()
                result = car.buscar_car()
                for carros in result:
                    print(f'ID: {carros[0]} | NOME_CAR: {carros[1]} | PLACA_CAR: {carros[2]} | ESTADO_PLACA: {carros[3]} |CHASSI_CAR: {carros[4]}')

                id_atualizar = int(input("Digite o ID do Carro que deseja atualizar: "))
                result = list(car.buscar_por_id_car(id_atualizar))
                result[1] = input("Digite o novo Nome do carro: ")
                result[2] = input("Digite a nova placa do carro: ")
                result[3] = input("Digite o novo estado da placa do carro: ")
                result[4] = input("Digite o novo chassi do carro: ")
                atualizacao = car.atualizar_car(tuple(result))
                if atualizacao == True:
                    print("Carro atualizado com sucesso!!!")