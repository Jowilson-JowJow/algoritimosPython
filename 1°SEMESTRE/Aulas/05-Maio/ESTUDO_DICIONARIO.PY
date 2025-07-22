# #Um dicionário é uma estrutura de dados que armazena pares chaves-valor. É muito útil qaundo queremos associar uma informação (valor) a uma etiqueta única (chave).

# aluno={'nome':"joão", 'idade': 20,'curso':'ADS'}
# print(f'O nome do aluno é {aluno['nome']}')
# print(f'A idade do aluno é {aluno['idade']}')
# print(f'O curso do aluno é {aluno[f'curso']}')

# # a sintaxe para criar um dicionario é (d={'chave':'valor'})

#====================================================

# #pode se criar dicionarios de 3 formas, veja abaixo:
# d1={"a":1,'b':2}
# d2=dict(c=3,d=4)
# d3=dict([('e',5),('f',6)])
# print(d1,d2,d3)

#====================================================

#para acesar elementos de um dicionario, basta usar a sintaxe:
# dados={'nome': 'ana', 'idade':25}
# print(dados['idade'])
# print(dados.get('nome'))
# print(dados.get('peso',0)) #retorna 0 se a chave nã existir

#====================================================

# # adicionando e removendo valores
# dados1={}#cria dicionario vazio
# print(dados1)
# dados1['nome']='ana'
# print(dados1)
# dados1['idade']=22
# print(dados1)
# dados1['idade']=23 #modifica o valor de 22 para 23
# print(dados1)

#====================================================

# # para remover itens do dicionario
# dados={'nome':'ana','idade':22}
# print(dados)
# del dados['idade'] #remove pela chave
# print(dados)
# nome=dados.pop('nome')
# print(dados, nome)# Remove e retorna o valor (teste a diferença com print(dados))

#====================================================

# #verifiand a existencia de chaves

# info={'curso':'python'}
# print('curso' in info) #retorna True
# print('nome' in info) #retorna False

#====================================================

# #inteirando sobre dicionários
# carro={'marca':'ford','modelo':'ka','ano':2020}
# for chave in carro:
#     print(chave, carro[chave],end=" ")

# for chave, valor in carro.items(): #dar preferncia para essa forma
#     print(chave, valor)

#====================================================

# #dict.keys()	Retorna todas as chaves
# #dict.values()	Retorna todos os valores
# #dict.items()	Retorna pares (chave, valor)
# #dict.update()	Atualiza o dicionário com outro
# #dict.clear()	Remove todos os itens
# #dict.copy()	Retorna uma cópia rasa (shallow copy)
# pessoa = {"nome": "João", "idade": 30}
# print(pessoa.keys())
# print(pessoa.values())
# print(pessoa.items())

# pessoa.update({"idade": 31, "cidade": "SP"})
# print(pessoa)

# nova = pessoa.copy()
# nova["nome"] = "Pedro"
# print(pessoa, nova)

#====================================================

# # dicionarios aninhados (nested dicts)
# usuarios = {
#     "user1": {"nome": "Ana", "idade": 28},
#     "user2": {"nome": "Paulo", "idade": 32}
# }

# print(usuarios["user1"]["nome"])  # Ana

#====================================================

# # compreensão de dicionarios (dic comprehension)
# quadrados = {x: x**2 for x in range(5)}
# print(quadrados)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#====================================================

# #conversã de outros tipos para dicionarios
# lista = [("a", 1), ("b", 2)]
# d = dict(lista)
# print(d)

# # De dois listas
# chaves = ["nome", "idade"]
# valores = ["Carlos", 20]
# d2 = dict(zip(chaves, valores))
# print(d2)

#====================================================

# #Uso de defaultdict (do módulo collections)
# from collections import defaultdict

# d = defaultdict(int)
# d["chave1"] += 1  # Inicializa automaticamente com 0
# print(d)

#====================================================

#Uso de Counter (frequência de elementos)
from collections import Counter

frase = "banana"
contagem = Counter(frase)
print(contagem)  # {'a': 3, 'b': 1, 'n': 2}

#====================================================

#Ordenação de Dicionários
d = {"c": 3, "a": 1, "b": 2}
ordenado = dict(sorted(d.items()))
print(ordenado)

#====================================================

#Dicionário como Estrutura de Dados (Casos práticos)
texto = "python é fácil e python é poderoso"
palavras = texto.split()
frequencia = {}

for palavra in palavras:
    frequencia[palavra] = frequencia.get(palavra, 0) + 1

print(frequencia)

#====================================================

# Boas Práticas com Dicionários
# Use chaves imutáveis (strings, números, tuplas).

# Prefira get() para evitar KeyError.

# Quando possível, use defaultdict para contagens.

# Use items() para percorrer pares chave-valor eficientemente.


 #grupo Jowilson, Yan e o Gustavo
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