# Crie uma classe para representar um hor´ ario (hora, minuto e segundo). Implemente os
# m´etodos para fazer as operac¸ ˜oes de incremento (de segundos) no hor´ ario e diferenc¸a
# entre dois hor´ arios.


class Horario:

    def __init__(self, hora, minuto, segundo):
        self.hora = hora % 24
        self.minuto = minuto % 60
        self.segundo = segundo % 60
        
        self.total_segundos = self.hora * 3600 + self.minuto * 60 + self.segundo
        self.total_segundos = self.total_segundos % 86400

    def __str__(self):
        h = self.total_segundos // 3600
        segundos_restantes = self.total_segundos % 3600
        m = segundos_restantes // 60
        s = segundos_restantes % 60

        return f"{h:02d}:{m:02d}:{s:02d}"

    def incrementar_segundos(self, segundos_a_adicionar):
        self.total_segundos += segundos_a_adicionar
        self.total_segundos = self.total_segundos % 86400
        print(f"Horário incrementado em {segundos_a_adicionar} segundos: {self}")

    def diferenca(self, outro_horario):
        diferenca_segundos = abs(self.total_segundos - outro_horario.total_segundos)

        horas, segundos_restantes = divmod(diferenca_segundos, 3600)
        minutos, segundos = divmod(segundos_restantes, 60)

        print(f"\nA diferença entre {self} e {outro_horario} é de:")
        print(f"-> {diferenca_segundos} segundos")
        print(f"-> {horas:02d} horas, {minutos:02d} minutos e {segundos:02d} segundos")

        return diferenca_segundos



horario_inicio = Horario(10, 30, 45)
horario_final = Horario(14, 5, 10)

print("--- Teste de Criação e Exibição ---")
print(f"Horário de Início: {horario_inicio}")
print(f"Horário Final: {horario_final}")

print("\n--- Teste de Incremento ---")
horario_inicio.incrementar_segundos(300)

print("\n--- Teste de Diferença ---")
horario_inicio.diferenca(horario_final)