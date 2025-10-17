class AlunoAcademia:
    def __init__(self, nome, idade, peso, altura):
        """Inicializa os atributos do aluno"""
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = 120

    def calcular_imc(self):
        """Calcula o Índice de Massa Corporal (IMC)"""
        imc = self.peso / (self.altura ** 2)
        return imc

    def obter_valor_mensalidade(self):
        """Retorna o valor da mensalidade, com desconto para menores de idade"""
        if self.idade < 18:
            valor_com_desconto = self.mensalidade * 0.9
            return valor_com_desconto
        else:
            return self.mensalidade

def main():
    nome = input("Informe o nome do aluno: ")
    idade = int(input("Informe a idade do aluno: "))
    peso = float(input("Informe o peso do aluno (em kg): "))
    altura = float(input("Informe a altura do aluno (em metros): "))

    aluno = AlunoAcademia(nome, idade, peso, altura)

    imc = aluno.calcular_imc()
    print(f"\nO IMC do aluno {aluno.nome} é: {imc:.2f}")

    mensalidade = aluno.obter_valor_mensalidade()
    print(f"O valor da mensalidade de {aluno.nome} é: R$ {mensalidade:.2f}")

if __name__ == "__main__":
    main()
