
class Estudante:#nome da classe, sempre deve iniciar com letra maiuscula.
    def __init__(self,nome,idade,nota):#método construtor.
        self.nome = nome #atributo
        self.idade = idade #atributo
        self.nota = nota #atributo

    def get_grade(self):
        print(self.nota)

e1 = Estudante("Luiz",20,10)
e2 = Estudante("Jow",22,10)

print(e1)# instancia é o endereço do variavel
print(e1.nome)
e1.get_grade()