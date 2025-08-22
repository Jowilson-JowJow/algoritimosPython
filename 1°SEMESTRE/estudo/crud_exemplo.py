# Classe que representa o objeto Usuário
class Usuario:
    def __init__(self, user_id, nome, email):
        self.id = user_id
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Email: {self.email}"


# Lista que será o "banco de dados em memória"
usuarios = []
id_counter = 1  # contador automático para IDs


def criar_usuario():
    global id_counter
    nome = input("Nome: ")
    email = input("Email: ")
    usuarios.append(Usuario(id_counter, nome, email))
    print("Usuário cadastrado com sucesso!")
    id_counter += 1


def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("\n--- Lista de Usuários ---")
        for u in usuarios:
            print(u)


def atualizar_usuario():
    user_id = int(input("Digite o ID do usuário a atualizar: "))
    for u in usuarios:
        if u.id == user_id:
            u.nome = input("Novo Nome: ")
            u.email = input("Novo Email: ")
            print("Usuário atualizado!")
            return
    print("Usuário não encontrado!")


def deletar_usuario():
    user_id = int(input("Digite o ID do usuário a excluir: "))
    for u in usuarios:
        if u.id == user_id:
            usuarios.remove(u)
            print("Usuário removido!")
            return
    print("Usuário não encontrado!")


# Menu principal
def menu():
    while True:
        print("\n==== MENU CRUD ====")
        print("1 - Criar Usuário")
        print("2 - Listar Usuários")
        print("3 - Atualizar Usuário")
        print("4 - Deletar Usuário")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            atualizar_usuario()
        elif opcao == "4":
            deletar_usuario()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")


# Executar programa
menu()
