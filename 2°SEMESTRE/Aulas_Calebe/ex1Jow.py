#Exercício 1 - Sistema de Agendamento (Clínica de Estética)


class Cliente:
    def __init__(self, nome, cpf, telefone, email, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def cadastrar(self):
        print(f"Cliente {self.nome} cadastrado com sucesso.")

    def atualizar_dados(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        print("Dados do cliente atualizados!")

    def visualizar_agendamentos(self):
        print(f"Mostrando agendamentos do cliente {self.nome}")


class Profissional:
    def __init__(self, nome, especialidade, registro_profissional, telefone, disponivel):
        self.nome = nome
        self.especialidade = especialidade
        self.registro_profissional = registro_profissional
        self.telefone = telefone
        self.disponivel = disponivel 

    def verificar_disponibilidade(self):
        if self.disponivel:
            print(f"{self.nome} está disponível para atendimento.")
        else:
            print(f"{self.nome} NÃO está disponível no momento.")

    def adicionar_horario(self, horario):
        print(f"Horário {horario} adicionado para o profissional {self.nome}")

    def remover_horario(self, horario):
        print(f"Horário {horario} removido para o profissional {self.nome}")


class Servico:
    def __init__(self, codigo_descricao, nome, descricao, duracao_min, preco):
        self.codigo_descricao = codigo_descricao
        self.nome = nome
        self.descricao = descricao
        self.duracao_min = duracao_min
        self.preco = preco

    def calcular_preco(self):
        return self.preco

    def atualizar_descricao(self, nova_desc):
        self.descricao = nova_desc
        print("Descrição do serviço atualizada!")

    def listar_servico(self):
        print(f"Serviço: {self.nome} | Preço: {self.preco:.2f} | Duração: {self.duracao_min} min")


class Agendamento:
    def __init__(self, codigo, data, hora, status):
        self.codigo = codigo
        self.data = data
        self.hora = hora
        self.status = status 

    def criar_agendamento(self):
        self.status = "confirmado"
        print(f"Agendamento {self.codigo} CONFIRMADO para {self.data} às {self.hora}")

    def cancelar_reserva(self):
        self.status = "cancelado"
        print(f"Agendamento {self.codigo} foi CANCELADO")

    def confirmar_reserva(self):
        self.status = "confirmado"
        print(f"Agendamento {self.codigo} CONFIRMADO novamente")


class Pagamento:
    def __init__(self, identificador, valor, forma_pagamento, data, status):
        self.identificador = identificador
        self.valor = valor
        self.forma_pagamento = forma_pagamento
        self.data = data
        self.status = status  

    def processar_pagamento(self):
        self.status = "Processando"
        print("Pagamento em processamento...")

    def verificar_status(self):
        print(f"Status do pagamento: {self.status}")

    def emitir_recibo(self):
        print(f"Recibo emitido: Valor R$ {self.valor:.2f} | Forma: {self.forma_pagamento} | Data: {self.data}")


cliente1 = Cliente("Ana", "123.456.789-10", "99999-0000", "ana@email.com", "Rua Flores, 10")
cliente1.cadastrar()

prof = Profissional("Marcos", "Esteticista", "CR-12345", "98888-1111", True)
prof.verificar_disponibilidade()

servico = Servico("S01", "Limpeza Facial", "Limpeza completa com máscaras", 60, 120.00)
servico.listar_servico()

ag = Agendamento("AG01", "12/11/2025", "14:00", "pendente")
ag.criar_agendamento()

pag = Pagamento("PG01", 120.00, "Cartão", "12/11/2025", "Pendente")
pag.processar_pagamento()
pag.verificar_status()
pag.emitir_recibo()