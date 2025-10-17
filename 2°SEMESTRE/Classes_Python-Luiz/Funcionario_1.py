class Funcionario_1:
    def __init__(self, nome, sobrenome, horas_trabalhadas, valor_hora):
        """Inicializa os atributos do funcionário"""
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def nomeCompleto(self):
        """Exibe o nome completo do funcionário"""
        print(f"Nome completo: {self.nome} {self.sobrenome}")

    def calcularSalario(self):
        """Calcula e exibe o salário do funcionário"""
        salario = self.horas_trabalhadas * self.valor_hora
        print(f"Salário do funcionário: R${salario:.2f}")

    def incrementarHoras(self, horas_adicionais):
        """Incrementa as horas trabalhadas"""
        self.horas_trabalhadas += horas_adicionais
        print(f"As horas trabalhadas foram incrementadas. Total de horas: {self.horas_trabalhadas}")

funcionario1 = Funcionario_1("Carlos", "Almeida", 160, 25)

funcionario1.nomeCompleto()  
funcionario1.calcularSalario()  
funcionario1.incrementarHoras(10)  
funcionario1.calcularSalario()
