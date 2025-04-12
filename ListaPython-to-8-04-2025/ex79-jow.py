#Crie uma lista e remova os espaços em branco dos elementos.
lista=['     lista','casa     ','         arv  o  r  e          ']
lista1=[x.strip() for x in lista]#SÓ TIRA O ESPAÇO ANTES OU APOS A PALAVRA E NÃO NO MEIO DA PALAVRA
print(lista)
print(lista1)
