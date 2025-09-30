###################HERANÇA E POLIMORFISMO #########################
class Funcionario:
    def __init__(self, nome, login, senha):
        self.nome = nome
        self.login=login
        self.senha = senha

    def logar(self):
        print(f"{self.nome} logado com sucesso")

    def set_senha(self, nova_senha):
        self.senha = nova_senha
        return True
    
class Gerente(Funcionario):
    def __init__(self, nome, login, senha, setor):
        super().__init__(nome, login, senha)
        self.setor =setor
    def logar(self):##polimorfismo
        confirm = input("digite o tokene")
        if confirm:
            print(f"Gerente {self.nome}logado com sucesso no setor: {self.setor}")

f1 = Funcionario("Eliandro", "lili@eli.com","1234")
f2 = Funcionario("Felix", "felix@eli.com","4321")

luan=Gerente("Luan Victor","lulu@gmail.com","1234","vendas")
luan.logar()
print(luan.senha)
luan.set_senha("7894")
print(luan.senha)