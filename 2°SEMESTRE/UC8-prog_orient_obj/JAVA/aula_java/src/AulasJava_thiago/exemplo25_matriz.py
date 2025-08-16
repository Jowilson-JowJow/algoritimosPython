
i=0#contador para percorrer linhas 
j=0#contador para percorrer colunas
matriz = []
lin = int(input("Digite a quantidade de linhas: "))
col = int(input("Digite a quantidade de colunas: "))
while i<lin:
    linha = []
    while j<col:
        if i==j:
            linha.append(1)
        else:
            linha.append(0)
        # num =1
        # linha.append(num)
        j=j+1
    matriz.append(linha)
    i=i+1
    j=0
print (matriz)