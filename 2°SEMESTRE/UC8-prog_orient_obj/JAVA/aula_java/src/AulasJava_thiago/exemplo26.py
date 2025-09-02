#funçãopara imprimir listas
pessoa={
    "nome":"jowjow",
    "idade":48,
    "cidade":"campo grande"
}
def verifica_cidade(dicionario:dict):
    if dicionario["cidade"]=="campo grande":
        return"É de campo grande"
    else:
        return f"é de {dicionario["cidade"]}"
    
# cidade=verifica_cidade(pessoa)
# print(cidade)


def imprime_lista(lista):
    for item in lista:
        print(item,end=" ")

# frutas=["banana", "mação", "pera"]
# carros=["gol","fusca","marajó"]
# tupla=(33,44,55,66,77,88,99,00)

# imprime_lista(tupla)
