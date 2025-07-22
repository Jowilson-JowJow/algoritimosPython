#Escreva uma função que embaralhe os caracteres de uma string (use random.shuffle).
import random
def embaralhar(lista):
    random.shuffle(lista)
    print(lista)

def menu():
    lista_palavra=[]
    while True:
        menu=int(input('Digite:\n1 -- para acrescentar uma palavra na lista\n2 -- para sair'))
        if menu==1:
            x=input('Digite uma palavra: ')
            lista_palavra.append(x)
        elif menu==2:
            break
        else:
            print('Digite 1 ou 2')

    embaralhar(lista_palavra)
menu()
    