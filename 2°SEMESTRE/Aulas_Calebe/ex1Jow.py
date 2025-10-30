#Exercício 1 - Sistema de Agendamento (Clínica de Estética)

class Cliente:
    def __init__ (self, nome, cpf, telefone, email, endereco):
        self.nome = nome 
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def cadastrar(self):
        print(f"Cliente: {self.nome} | CPF: {self.cpf}\nCadastrado com Sucesso!!!")

    def atualizar(self, nome, email , telefone, endereco):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def ver_agendamento(self):


class Servico:
    def __init__(self, codigo, nome, descricao, duracao, preco):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.duracao = duracao
        self.preco = preco

    def calcular_preco(self):

    def atualisar_descricao(self):

    def lista_servico(self):


class Profissional:
    def __init__(self, nome, especialidade, registro_profissional, telefone, disponivel):
        self.nome = nome
        self.especialidade = especialidade
        self.registro_profissional = registro_profissional
        self.telefone = telefone
        self.disponivel = disponivel

    def ver_disponibilidade(self):

    def add_horario(self):


    def remove_horario(self):


class Agendamento:
    def __init__(self, codigo, data, hora, status):
        self.codigo = codigo
        self.data = data
        self.hora = hora
        self.status = status

    def criar_agendamento(self):


    def cancelar_reserva(self):


    def comfirmar_reserva(self):


class Pagamento:
    def __init__(self, codigo, valor, forma_pagamento, data, status):
        self.codigo = codigo
        self.valor = valor
        self.forma_pagamento = forma_pagamento
        self.data = data
        self.status = status

    def processar_pagamento(self):

    def ver_status(self):

    def emitir_recibo(self):
        

# comite hoje