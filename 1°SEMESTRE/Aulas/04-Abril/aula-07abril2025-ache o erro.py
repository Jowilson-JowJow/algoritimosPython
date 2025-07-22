print("-- Reservatório de Água --")#corrigi a palavra reservatório e coloque o parênteses no final do codigo

altura=int(input(" Digite a altura (cm):"))#troquei float por int
largura=int(input(" Digite a largura (cm): "))#acrescentei o ultimpareteses que faltava
comprimento=int(input(" Digite o comprimento (cm): "))#troquei float por int
c_diario=int(input("Digite o valor do consumo médio diário(litros/dia)= "))#acrescente o sinal de igual e troquei float por int e tirei o acento do á

cap_total=((altura*largura*comprimento)/1000); #o resultado seria em cm3 por isso, dividimos por mil para passar de cm3 para litros #troquei a virgula por multiplicação entre a largura e comprimento e troquei o ''' ''' por # para comentar
auton_reser=cap_total/c_diario

print("Capacidade do Reservatório= ",cap_total, "litros ")
print("Autonomia do reservatório= ",auton_reser," dias") #Agora, vamos classificar o consumo #troquei o ''' ''' por # para comentar
if(auton_reser<2):
    print("Consumo Elevado")#acrescentei o 4 espaço
elif(auton_reser>=2 and auton_reser<7):# coloquei o sinal de menor no 7
     print("Consumo Moderado")
elif(auton_reser>7):
    print("\n Consumo Baixo")#tirei o excesso de espaços

print("achei todos os erro, acadêmico Jowilson")