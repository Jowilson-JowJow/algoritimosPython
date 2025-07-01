 #grupo: Gustavo Rosa dos Santos -- Jowilson Ribas Nunes -- Yan Torres Martins 
def salvar_clientes():
    f = open("clientes.txt", "w")
    for c in clientes:
        cpf, nome, tel = c.split(";")
        linha = f"CPF: {cpf}; Nome: {nome}; Tel: {tel}\n"
        f.write(linha)
    f.close()
 
def salvar_veiculos():
    f = open("veiculos.txt", "w")
    for v in veiculos:
        placa, modelo, ano, cpf = v.split(";")
        linha = f"Placa: {placa}; Modelo: {modelo}; Ano: {ano}; CPF: {cpf}\n"
        f.write(linha)
    f.close()
 
def salvar_os():
    f = open("os.txt", "w")
    for o in ordens:
        num, desc, valor, cpf, placa = o.split(";")
        linha = f"OS: {num}; Descrição: {desc}; Valor: {valor}; CPF: {cpf}; Placa: {placa}\n"
        f.write(linha)
    f.close()
 
def carregar(arquivo):
    try:
        f = open(arquivo, "r")
        linhas = [linha.strip() for linha in f.readlines()]
        f.close()
        return linhas
    except:
        return []
 
 
def cadastrar_cliente():
    cpf = input("CPF: ")
    nome = input("Nome: ")
    tel = input("Telefone: ")
    for c in clientes:
        if c.split(";")[0] == cpf:
            print("CPF já existe.")
            return
    clientes.append(f"{cpf};{nome};{tel}")
    salvar_clientes()
    print("Cliente cadastrado.")
 
def listar_clientes():
    for c in clientes:
        print(c)
 
def editar_cliente():
    cpf = input("CPF do cliente: ")
    for i in range(len(clientes)):
        if clientes[i].split(";")[0] == cpf:
            nome = input("Novo nome: ")
            tel = input("Novo telefone: ")
            clientes[i] = f"{cpf};{nome};{tel}"
            salvar_clientes()
            print("Cliente atualizado.")
            return
    print("Cliente não encontrado.")
 
def excluir_cliente():
    cpf = input("CPF do cliente: ")
    nova = [c for c in clientes if c.split(";")[0] != cpf]
    if len(nova) < len(clientes):
        clientes[:] = nova
        veiculos[:] = [v for v in veiculos if v.split(";")[3] != cpf]
        ordens[:] = [o for o in ordens if o.split(";")[3] != cpf]
        salvar_clientes()
        salvar_veiculos()
        salvar_os()
        print("Cliente e dados vinculados removidos.")
    else:
        print("CPF não encontrado.")
 
 
def cadastrar_veiculo():
    placa = input("Placa: ")
    modelo = input("Modelo: ")
    ano = input("Ano: ")
    cpf = input("CPF do dono: ")
    if not any(c.split(";")[0] == cpf for c in clientes):
        print("CPF não cadastrado.")
        return
    if any(v.split(";")[0] == placa for v in veiculos):
        print("Placa já cadastrada.")
        return
    veiculos.append(f"{placa};{modelo};{ano};{cpf}")
    salvar_veiculos()
    print("Veículo cadastrado.")
 
def listar_veiculos():
    for v in veiculos:
        print(v)
 
def editar_veiculo():
    placa = input("Placa: ")
    for i in range(len(veiculos)):
        if veiculos[i].split(";")[0] == placa:
            modelo = input("Novo modelo: ")
            ano = input("Novo ano: ")
            cpf = veiculos[i].split(";")[3]
            veiculos[i] = f"{placa};{modelo};{ano};{cpf}"
            salvar_veiculos()
            print("Veículo atualizado.")
            return
    print("Veículo não encontrado.")
 
def excluir_veiculo():
    placa = input("Placa: ")
    nova = [v for v in veiculos if v.split(";")[0] != placa]
    if len(nova) < len(veiculos):
        veiculos[:] = nova
        ordens[:] = [o for o in ordens if o.split(";")[4] != placa]
        salvar_veiculos()
        salvar_os()
        print("Veículo e OS removidas.")
    else:
        print("Placa não encontrada.")
 
 
def cadastrar_os():
    num = input("Número da OS: ")
    desc = input("Descricao: ")
    valor = input("Valor: ")
    cpf = input("CPF: ")
    placa = input("Placa: ")
    if not any(c.split(";")[0] == cpf for c in clientes):
        print("CPF inválido.")
        return
    if not any(v.split(";")[0] == placa for v in veiculos):
        print("Placa inválida.")
        return
    if any(o.split(";")[0] == num for o in ordens):
        print("Número de OS já existe.")
        return
    ordens.append(f"{num};{desc};{valor};{cpf};{placa}")
    salvar_os()
    print("OS cadastrada.")
 
def listar_os():
    for o in ordens:
        print(o)
 
def editar_os():
    num = input("Número da OS: ")
    for i in range(len(ordens)):
        if ordens[i].split(";")[0] == num:
            desc = input("Nova descricao: ")
            valor = input("Novo valor: ")
            cpf = ordens[i].split(";")[3]
            placa = ordens[i].split(";")[4]
            ordens[i] = f"{num};{desc};{valor};{cpf};{placa}"
            salvar_os()
            print("OS atualizada.")
            return
    print("OS não encontrada.")
 
def excluir_os():
    num = input("Número da OS: ")
    nova = [o for o in ordens if o.split(";")[0] != num]
    if len(nova) < len(ordens):
        ordens[:] = nova
        salvar_os()
        print("OS removida.")
    else:
        print("OS não encontrada.")
 
def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Editar Cliente")
        print("4 - Excluir Cliente")
        print("5 - Cadastrar Veículo")
        print("6 - Listar Veículos")
        print("7 - Editar Veículo")
        print("8 - Excluir Veículo")
        print("9 - Cadastrar OS")
        print("10 - Listar OS")
        print("11 - Editar OS")
        print("12 - Excluir OS")
        print("0 - Sair")
        op = input("Opção: ")
 
        match op:
            case "1": cadastrar_cliente()
            case "2": listar_clientes()
            case "3": editar_cliente()
            case "4": excluir_cliente()
            case "5": cadastrar_veiculo()
            case "6": listar_veiculos()
            case "7": editar_veiculo()
            case "8": excluir_veiculo()
            case "9": cadastrar_os()
            case "10": listar_os()
            case "11": editar_os()
            case "12": excluir_os()
            case "0":
                print("Saindo.")
                break
            case _:
                print("Opção inválida.")
 
        input("\nPressione Enter para voltar ao menu...")
 
clientes = carregar("clientes.txt")
veiculos = carregar("veiculos.txt")
ordens = carregar("os.txt")
 

menu() 