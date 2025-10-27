#Exercício 1 - Sistema de Agendamento (Clínica de Estética)

# from datetime import date, time

# class Cliente:
#     def __init__ (self, nome, cpf, telefone, email, endereco):
#         self.nome = nome
#         self.cpf = cpf
#         self.telefone = telefone
#         self.email = email
#         self.endereco = endereco
#         self.agendamentos =[]

#     def cadastrar(self):


from datetime import date, time


class Cliente:
    def __init__(self, nome, cpf, telefone, email, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.agendamentos = []

    def cadastrar(self):
        print(f"Cliente {self.nome} cadastrado com sucesso!")

    def atualizar_dados(self, telefone=None, email=None, endereco=None):
        if telefone:
            self.telefone = telefone
        if email:
            self.email = email
        if endereco:
            self.endereco = endereco
        print(f"Dados de {self.nome} atualizados!")

    def visualizar_agendamentos(self):
        print(f"\nAgendamentos de {self.nome}:")
        if not self.agendamentos:
            print("Nenhum agendamento encontrado.")
        for ag in self.agendamentos:
            print(f" - {ag.data} às {ag.hora}, com {ag.profissional.nome}, Status: {ag.status}")


class Profissional:
    def __init__(self, nome, especialidade, registro_profissional, telefone, disponivel=True):
        self.nome = nome
        self.especialidade = especialidade
        self.registro_profissional = registro_profissional
        self.telefone = telefone
        self.disponivel = disponivel
        self.horarios = []

    def verificar_disponibilidade(self, data_ag, hora_ag):
        if (data_ag, hora_ag) in self.horarios:
            print(f"{self.nome} NÃO está disponível em {data_ag} {hora_ag}.")
            return False
        print(f"{self.nome} está disponível em {data_ag} {hora_ag}.")
        return True

    def adicionar_horario(self, data_ag, hora_ag):
        self.horarios.append((data_ag, hora_ag))
        print(f"Horário {data_ag} {hora_ag} adicionado para {self.nome}.")

    def remover_horario(self, data_ag, hora_ag):
        if (data_ag, hora_ag) in self.horarios:
            self.horarios.remove((data_ag, hora_ag))
            print(f"Horário {data_ag} {hora_ag} removido para {self.nome}.")


class Servico:
    def __init__(self, codigo, nome, descricao, duracao_min, preco):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.duracao_min = duracao_min
        self.preco = preco

    def calcular_preco(self):
        return self.preco

    def atualizar_descricao(self, nova_desc):
        self.descricao = nova_desc
        print(f"Descrição do serviço '{self.nome}' atualizada.")

    def listar_servico(self):
        print(f"Serviço: {self.codigo} - {self.nome} | {self.duracao_min} min | R$ {self.preco:.2f}")


class Pagamento:
    def __init__(self, valor, forma_pagamento, data_pagamento=date.today()):
        self.identificador = "PG" + str(int(date.today().strftime("%d%m%y%H%M%S")))
        self.valor = valor
        self.forma_pagamento = forma_pagamento
        self.data = data_pagamento
        self.status = "Pendente"

    def processar_pagamento(self):
        print(f"Processando pagamento de R$ {self.valor:.2f} via {self.forma_pagamento}...")
        self.status = "Concluido"
        print("Pagamento realizado com sucesso!")

    def verificar_status(self):
        print(f"Status do pagamento: {self.status}")

    def emitir_recibo(self):
        if self.status == "Concluido":
            print(f"Recibo emitido - Valor: R$ {self.valor:.2f} - Forma: {self.forma_pagamento}")
        else:
            print("Pagamento ainda não concluído, não é possível emitir recibo.")


class Agendamento:
    def __init__(self, cliente, profissional, data_ag, hora_ag, servicos):
        self.codigo = "AG" + str(int(date.today().strftime("%d%m%y%H%M%S")))
        self.cliente = cliente
        self.profissional = profissional
        self.data = data_ag
        self.hora = hora_ag
        self.servicos = servicos
        self.pagamento = None
        self.status = "Confirmado"

        cliente.agendamentos.append(self)
        profissional.adicionar_horario(data_ag, hora_ag)
        print(f"Agendamento criado para {cliente.nome} com {profissional.nome} em {data_ag} {hora_ag}.")

    def criar_agendamento(self):
        print(f"Agendamento {self.codigo} criado com sucesso!")

    def cancelar_reserva(self):
        self.status = "Cancelado"
        self.profissional.remover_horario(self.data, self.hora)
        print(f"Agendamento {self.codigo} cancelado.")

    def confirmar_reserva(self):
        self.status = "Confirmado"
        print(f"Agendamento {self.codigo} confirmado!")

    def calcular_total(self):
        return sum(serv.preco for serv in self.servicos)

    def registrar_pagamento(self, forma_pagamento):
        total = self.calcular_total()
        self.pagamento = Pagamento(total, forma_pagamento)
        print(f"Pagamento criado no valor de R$ {total:.2f} para o agendamento {self.codigo}.")

    def detalhes(self):
        print("\n--- Detalhes do Agendamento ---")
        print(f"Cliente: {self.cliente.nome}")
        print(f"Profissional: {self.profissional.nome}")
        print(f"Data: {self.data}, Hora: {self.hora}")
        print("Serviços:")
        for serv in self.servicos:
            print(f" - {serv.nome}: R$ {serv.preco:.2f}")
        print(f"Total: R$ {self.calcular_total():.2f}")
        print(f"Status: {self.status}")
        if self.pagamento:
            print(f"Pagamento: {self.pagamento.forma_pagamento}, {self.pagamento.status}")
        else:
            print("Pagamento ainda não realizado.")


# ========== EXEMPLO DE USO ==========
if __name__ == "__main__":
    # Criar cliente e profissional
    cliente = Cliente("Ana Pereira", "12345678900", "99999-9999", "ana@email.com", "Rua A, 123")
    profissional = Profissional("Mariana Lima", "Esteticista", "CR9876", "98888-8888")

    # Criar serviços
    serv1 = Servico("S001", "Limpeza de Pele", "Limpeza facial profunda", 60, 120.0)
    serv2 = Servico("S002", "Hidratação", "Hidratação facial", 30, 80.0)

    # Criar agendamento
    ag = Agendamento(cliente, profissional, date(2025, 11, 10), time(14, 30), [serv1, serv2])
    ag.detalhes()

    # Registrar e processar pagamento
    ag.registrar_pagamento("Cartão de crédito")
    ag.pagamento.processar_pagamento()
    ag.pagamento.emitir_recibo()

    # Mostrar agendamentos do cliente
    cliente.visualizar_agendamentos()
