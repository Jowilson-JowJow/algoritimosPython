import calendar

class Agenda:
    def __init__(self, dia, mes, ano):
        """Inicializa os atributos da agenda com data"""
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = None 

    def validar_data(self):
        """Valida se a data fornecida é válida"""
        if self.mes < 1 or self.mes > 12:
            print("Mês inválido! Deve ser entre 1 e 12.")
            return False
        
        dias_no_mes = calendar.monthrange(self.ano, self.mes)[1]  
        if self.dia < 1 or self.dia > dias_no_mes:
            print(f"Dia inválido! O mês {self.mes} de {self.ano} tem apenas {dias_no_mes} dias.")
            return False
        
        print("Data válida!")
        return True

    def anotar_tarefa(self, anotacao):
        """Anota uma tarefa para o dia especificado"""
        self.anotacao = anotacao
        print(f"Tarefa anotada para {self.dia}/{self.mes}/{self.ano}: {anotacao}")

    def mostrar_anotacao(self):
        """Exibe a anotação ou tarefa para o dia"""
        if self.anotacao:
            print(f"Anotação para {self.dia}/{self.mes}/{self.ano}: {self.anotacao}")
        else:
            print(f"Não há anotação para {self.dia}/{self.mes}/{self.ano}.")

agenda1 = Agenda(25, 12, 2023)

agenda1.validar_data()  

agenda1.anotar_tarefa("Comprar presentes de Natal")  

agenda1.mostrar_anotacao()  