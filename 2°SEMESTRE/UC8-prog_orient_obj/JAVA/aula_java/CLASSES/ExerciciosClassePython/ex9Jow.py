# 9 - Classe Aluno_Academia: Uma academia mantem registro de seus alunos e precisa armazenar os seguintes atributos:
# Nome, Idade, Peso, Altura, Mensalidade (valor default: R$ 120,00)
# A academia faz um desconto especial para menores de idade, portanto, é necessário saber distinguir entre um aluno maior e menor. Além disso, a academia também tem interesse em acompanhar o desempenho de seus alunos, por isso, ela também necessita conhecer o índice de massa corporal (IMC) deles, para isso a classe deve ter os seguintes métodos:
# Calcular_IMC()
# Obter_valor_mensalidade()

class Aluno_Academia:
    def __init__(self, nome, idade, peso, altura, mensalidade):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.altura=altura
        self.mensalidade=120