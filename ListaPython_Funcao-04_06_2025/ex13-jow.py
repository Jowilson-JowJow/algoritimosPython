#Crie uma função que receba uma string e retorne a mesma string sem espaços.
def palavras_sem_espacos (texto):
    texto_sem_espacos=texto.replace(' ','')
    print(texto_sem_espacos)

texto=input('digite uma frase: ')
palavras_sem_espacos(texto)