# 5 - Classe Funcionário: Uma empresa quer criar um controle de pagamento para os funcionários. Crie uma classe que modele um Funcionário com os seguintes atributos e métodos:
# Nome; Sobrenome; Horas_trabalhadas; Valor_hora;
# A classe deve ter o seguintes métodos:
# O método nomeCompleto deve escrever na tela o atributo nome concatenado ao atributo sobrenome.
# O método calcularSalario faz o cálculo de quanto o funcionário irá receber no mês, multiplicando o atributo horasTrabalhadas pelo atributo valorPorHora. Em seguida, escreve o valor na tela.
# O método incrementarHoras adiciona um valor passado por parâmetro ao valor já existente no atributo valorPorHora.

class Funcionario:
    def __init__(self, nome, sobrenome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora
    
    def nomeCompleto(self):
        print(f"{self.nome} {self.sobrenome}")

    def calcularSalario(self):
        return self.valor_hora * self.horas_trabalhadas
    
    def incrementarHoras(self, hora_adicionais):
        self.horas_trabalhadas += hora_adicionais
        return self.valor_hora * self.horas_trabalhadas
        

func1 = Funcionario("adriano","almeida paixão", 200, 10)
func1.nomeCompleto()
print(f"Salario: {func1.calcularSalario():.2f}")
print(f"Salario: {func1.incrementarHoras(10):.2f}")
