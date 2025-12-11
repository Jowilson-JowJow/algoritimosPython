#https://chatgpt.com/share/6938352a-c404-800c-8794-92919968abc3
# o link acima é a pesquisa que fi feita sobre as ordens de prcessos feitos pelo processador para escolher qual ordem será executado os precessos no processador, abaixo temos o exemplo de codigo de cada um dos tipos encontrado na pesquisa




def fifo(processos):
    tempo_atual = 0
    for nome, duracao in processos:
        print(f"Executando {nome} por {duracao}s")
        tempo_atual += duracao
    print("Todos os processos foram concluídos.")

processos = [("P1", 8), ("P2", 4), ("P3", 1)]
fifo(processos)

#===============================================

def sjf(processos):
    processos_ordenados = sorted(processos, key=lambda x: x[1])
    tempo = 0
    for nome, duracao in processos_ordenados:
        print(f"Executando {nome} por {duracao}s")
        tempo += duracao
    print("Finalizado.")

processos = [("P1", 6), ("P2", 2), ("P3", 8), ("P4", 3)]
sjf(processos)

#===============================================

from collections import deque

def round_robin(processos, quantum):
    fila = deque(processos)

    while fila:
        nome, tempo = fila.popleft()
        if tempo > quantum:
            print(f"{nome} executou {quantum}s e voltou para fila.")
            fila.append((nome, tempo - quantum))
        else:
            print(f"{nome} finalizou executando {tempo}s.")

processos = [("P1", 5), ("P2", 3), ("P3", 1)]
round_robin(processos, 2)

#===============================================

def prioridade(processos):
    processos_ordenados = sorted(processos, key=lambda x: x[1], reverse=True)
    for nome, prio in processos_ordenados:
        print(f"Executando {nome} com prioridade {prio}")

processos = [("P1", 3), ("P2", 1), ("P3", 2)]
prioridade(processos)


#===============================================

def garantido(processos, tempos_recebidos):
    # processos = ["P1", "P2", "P3"]
    # tempos_recebidos = [5, 1, 3]
    processos_ordenados = sorted(
        zip(processos, tempos_recebidos),
        key=lambda x: x[1]
    )

    escolhido = processos_ordenados[0][0]
    print(f"Processo escolhido: {escolhido}")

processos = ["P1", "P2", "P3"]
tempos = [5, 1, 3]
garantido(processos, tempos)


#===============================================

def tempo_compartilhado(processos, quantum):
    from collections import deque
    fila = deque(processos)

    while fila:
        nome, tempo = fila.popleft()
        exec_time = min(quantum, tempo)
        print(f"{nome} executou {exec_time}s")

        if tempo - quantum > 0:
            # prioridade dinâmica: quem executou volta com menor prioridade (fim da fila)
            fila.append((nome, tempo - quantum))

processos = [("P1", 7), ("P2", 4), ("P3", 2)]
tempo_compartilhado(processos, quantum=1)

