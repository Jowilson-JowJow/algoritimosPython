# #simular uma urna eletronica. 1,2,3,4 votos candidatos/ 5 voto nulo /6 voto em branco / 0 finaliza o programa e ai imprima total de votos para cada candidato/ total de votos nulos/ total de votos em branco
# cand1=0
# cand2=0
# cand3=0
# cand4=0
# branco=0
# nulo=0
# while True:
#     voto=int(input('A votação iniciou: \nDigite 1 -- para o candidato João Canabrava\nDigite 2 -- para a candidata florentina de jesus\nDigite 3 -- para o candidato Jhon Rambo\nDigite 4 -- para a candidata mãe do stifler\nDigite 5 -- para voto nulo\nDigite 6 -- para voto em branco\n'))
#     if voto==1:
#         cand1 +=1
#     elif voto==2:
#         cand2 +=1
#     elif voto==3:
#         cand3 +=1
#     elif voto==4:
#         cand4 +=1
#     elif voto==5:
#         branco +=1
#     elif voto==6:
#         nulo +=1
#     elif voto==0:
#         print('João Canabrava teve: ', cand1, 'votos')
#         print('florentina de jesus teve: ', cand2, 'votos')
#         print('jhon rambo teve: ', cand3, 'votos')
#         print('mãe do stifler teve: ', cand4, 'votos')
#         print('votos nulos teve: ', nulo, 'votos')
#         print('votos em branco teve: ', branco, 'votos')
#         break
#     else:
#         print("Voto inválido! Digite um número entre 1 e 6.")


# # Dicionário com os candidatos e votos
# votos = {
#     1: {'nome': 'João Canabrava', 'total': 0},
#     2: {'nome': 'Florentina de Jesus', 'total': 0},
#     3: {'nome': 'Jhon Rambo', 'total': 0},
#     4: {'nome': 'Mãe do Stifler', 'total': 0},
#     5: {'nome': 'Voto Nulo', 'total': 0},
#     6: {'nome': 'Voto em Branco', 'total': 0}
# }

# print("A votação iniciou!")

# while True:
#     try:
#         voto = int(input(
#             "\nDigite 1 -- João Canabrava\n"
#             "Digite 2 -- Florentina de Jesus\n"
#             "Digite 3 -- Jhon Rambo\n"
#             "Digite 4 -- Mãe do Stifler\n"
#             "Digite 5 -- Voto Nulo\n"
#             "Digite 6 -- Voto em Branco\n"
#             "Digite 0 -- Encerrar votação\n"
#             "Seu voto: "
#         ))

#         if voto == 0:
#             print("\n*** RESULTADO FINAL ***")
#             for chave in range(1, 7):
#                 print(f"{votos[chave]['nome']} recebeu {votos[chave]['total']} voto(s).")
#             break
#         elif voto in votos:
#             votos[voto]['total'] += 1
#         else:
#             print("Voto inválido. Digite um número entre 0 e 6.")

#     except ValueError:
#         print("Entrada inválida. Digite um número inteiro.")


# Lista de candidatos e tipos de voto
candidatos = [
    "João Canabrava",         # índice 0 (para voto 1)
    "Florentina de Jesus",    # índice 1 (para voto 2)
    "Jhon Rambo",             # índice 2 (para voto 3)
    "Mãe do Stifler",         # índice 3 (para voto 4)
    "Voto Nulo",              # índice 4 (para voto 5)
    "Voto em Branco"          # índice 5 (para voto 6)
]

# Lista para armazenar total de votos (inicialmente todos zero)
votos = [0] * len(candidatos)  # [0, 0, 0, 0, 0, 0]

print("A votação iniciou!")

while True:
    try:
        voto = int(input(
            "\nDigite 1 -- João Canabrava\n"
            "Digite 2 -- Florentina de Jesus\n"
            "Digite 3 -- Jhon Rambo\n"
            "Digite 4 -- Mãe do Stifler\n"
            "Digite 5 -- Voto Nulo\n"
            "Digite 6 -- Voto em Branco\n"
            "Digite 0 -- Encerrar votação\n"
            "Seu voto: "
        ))

        if voto == 0:
            print("\n*** RESULTADO FINAL ***")
            for i in range(len(candidatos)):
                print(f"{candidatos[i]} recebeu {votos[i]} voto(s).")
            break
        elif 1 <= voto <= 6:
            votos[voto - 1] += 1  # ajuste do índice (1 → 0, 2 → 1, ..., 6 → 5)
        else:
            print("Voto inválido. Digite um número entre 0 e 6.")

    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")




