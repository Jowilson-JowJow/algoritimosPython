# f=open("Aulas/05-maio/word.txt", "r")
# print(f.read())
# f.close()

# z=open("Aulas/05-maio/word.txt", "a", encoding="utf-8") #nesse caso ele apenas acrescenta o texto novo apos o texto antigo
# x=input('Digite seu nome:')
# z.write(f'\n{x}')
# z=open("Aulas/05-maio/word.txt", "r")
# print(z.read())
# z.close()

# z=open("Aulas/05-maio/word.txt", "w", encoding="utf-8") #nesse caso ele apaga o que tem antes e coloca o que foi novo
# x=input('Digite seu nome:')
# z.write(f'\n{x}')
# z=open("Aulas/05-maio/word.txt", "r")
# print(z.read())
# z.close()


# z=open("Aulas/05-maio/word1.txt", "x", encoding="utf-8") #cria arquivo especificado, retorna erro se o arquivo existir, deve ser usado para não subscrever
# x=input('Digite seu nome:')
# z.write(f'\n{x}')
# z=open("Aulas/05-maio/word1.txt", "r")
# print(z.read())
# z.close()

# z=open("Aulas/05-maio/word1.txt", "rt", encoding="utf-8") #'t' modo texto e 'b' modo binario (imagens)
# x=input('Digite seu nome:')
# z.write(f'\n{x}')
# z=open("Aulas/05-maio/word1.txt", "r")
# print(z.read())
# z.close()

z=open("Aulas/05-maio/naruto.jpg", "rb") #'t' modo texto e 'b' modo binario (imagens)
print(z.read())
z.close()
