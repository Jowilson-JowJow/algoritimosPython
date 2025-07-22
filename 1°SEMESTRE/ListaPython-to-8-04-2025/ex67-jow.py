#Crie uma lista de frases e utilize .split() para transformar cada frase em lista de palavras.
lista=['matemática', 'só', 'não', 'é', 'melhor', 'que', 'física']
frase=[x.split() for x in lista]
print(frase)