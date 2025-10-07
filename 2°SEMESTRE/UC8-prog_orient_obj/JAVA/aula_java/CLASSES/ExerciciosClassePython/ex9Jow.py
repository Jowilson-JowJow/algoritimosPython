# 9 - Classe Aluno_Academia: Uma academia mantem registro de seus alunos e precisa armazenar os seguintes atributos:
# Nome, Idade, Peso, Altura, Mensalidade (valor default: R$ 120,00)
# A academia faz um desconto especial para menores de idade, portanto, é necessário saber distinguir entre um aluno maior e menor. Além disso, a academia também tem interesse em acompanhar o desempenho de seus alunos, por isso, ela também necessita conhecer o índice de massa corporal (IMC) deles, para isso a classe deve ter os seguintes métodos:
# Calcular_IMC()
# Obter_valor_mensalidade()

class Aluno_Academia:
    def __init__(self, nome, idade, peso, altura):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.altura=altura
        self.mensalidade=120

    def calcular_IMC(self):
        return self.peso/(self.altura**2)
    
    def valor_mensalidade(self):
        if (self.idade<18):
            return self.mensalidade*0.9
        else:
            return self.mensalidade

aluno1=Aluno_Academia("joão",17,80,1.78,)
aluno2=Aluno_Academia("Lucas",19,90,1.82,)

imc1=aluno1.calcular_IMC()
imc2=aluno2.calcular_IMC()
mensalidade1=aluno1.valor_mensalidade()
mensalidade2=aluno2.valor_mensalidade()
print(f"O aluno {aluno1.nome} tem imc igual a {imc1:.2f}")
print(f"O aluno {aluno2.nome} tem imc igual a {imc2:.2f}")
print(f"A mensalidade do aluno {aluno1.nome} é R$ {mensalidade1}")
print(f"A mensalidade do aluno {aluno2.nome} é R$ {mensalidade2}")

