# 7 - Classe Agenda: crie uma classe que represente uma agenda de tarefas.
# Esta classe deve possuir os seguintes atributos:
# Dia; Mês; Ano; Anotação;
# A classe deve ter os seguintes métodos:
# validar_data(); anotar_tarefa(); mostrar_anotacao();

class Agenda:
    def __init__(self, dia, mes, ano, anotacao):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao

    def validar_data(self):
        if (self.mes < 1 or self.mes > 12):
            return False
        
        dias_por_mes = [
            31,
            29 if (self.ano % 4 == 0 and (self.ano % 100 != 0 or self.ano % 400 == 0)) else 28,
            31, 30, 31, 30, 31, 31, 30, 31, 30, 31
        ]

        if (self.dia < 1 or self.dia > dias_por_mes[self.mes - 1]):
            return False

        return True

    def anotar_tarefa(self):
        self.anotacao = input("Digite a nova anotação/tarefa: ")
        print("Tarefa anotada com sucesso!")

    def mostrar_anotacao(self):
        print(f"\nData: {self.dia:02d}/{self.mes:02d}/{self.ano}")
        print(f"Anotação: {self.anotacao}\n")



agenda = Agenda(15, 10, 2025, "Entrega do projeto de Python")

if agenda.validar_data():
    print("Data válida!")
    agenda.mostrar_anotacao()
    agenda.anotar_tarefa()
    agenda.mostrar_anotacao()
else:
    print("Data inválida!")
