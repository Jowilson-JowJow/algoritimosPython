#Crie uma lista de palavras e remova todas que tenham mais de 6 letras.
lista = ['ar','sol','fogo','vento','nuvens','neblina','climático','chuvisco','granizo','chuva']
lista1=[x for x in lista if len(x)<=5]
print(lista1)