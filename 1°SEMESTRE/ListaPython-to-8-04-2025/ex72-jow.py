#Crie uma lista de frases e extraia a primeira palavra de cada frase.
lista=["A física explica o mundo","Matemática é a linguagem do universo","A energia se transforma","Ondas transportam energia"]
primeira_frase=[lista.split()[0] for lista in lista]
print(primeira_frase)
primeira_frase=[lista.split()[1] for lista in lista]
print(primeira_frase)
