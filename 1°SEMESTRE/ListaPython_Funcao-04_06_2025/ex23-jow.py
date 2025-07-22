#Escreva uma função que receba uma frase e retorne a quantidade de palavras.
def num_palavras(frase):
    palavras=frase.split() # serve para separar palavras de uma frase em uma lista de palavras.
    total_palavras=len(palavras)#retorna o tamanho da lista
    print(f'O frase escrita {frase}, possui {total_palavras} palavras escritas')

x=input('Digite uma frase ou oração: ')
num_palavras(x)    
