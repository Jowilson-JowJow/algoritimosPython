#nome, cpf, fone, email, cidade, estado
#metodos printar tudo
class Pessoa:
    def __init__(self,nome,cpf,fone,email,cidade,estado):
        self.nome = nome
        self.cpf = cpf
        self.fone = fone
        self.email = email
        self.cidade = cidade
        self.estado = estado

    def nomes(self):
        print(self.nome)
    def cpfs(self):
        print(self.cpf)
    def fones(self):
        print(self.fone)
    def emails(self):
        print(self.email)
    def cidades(self):
        print(self.cidade)
    def estados(self):
        print(self.estado)

pessoa = Pessoa("JowJow","78955815115","(67)992145281","jowfisico@yahoo.com.br","campo grande","MS")
pessoa.nomes()
pessoa.cpfs()
pessoa.fones()
pessoa.emails()
pessoa.cidades()
pessoa.estados()

