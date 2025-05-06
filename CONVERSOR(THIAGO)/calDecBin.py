# #algoritmo para calcular decimal para binario
# valor=29
# novo_val=valor%2
# print(novo_val)
# valor=valor/2
# print(int(valor)) #ou valor=valor//2 ai nesse caso é colocado print(valor)
# #linhas 2,3,4,5,6 foram apenas teste

import os
valor=float(input('Digite um valor em decimal para converter em binario:'))
valor_binario=[]
cont=0
while valor >0:
    cont+=1
    novoValor=valor%2
    novoValor = int(novoValor)
    print('Resto: ',novoValor)
    valor=valor/2
    print('Divisor: ', valor)
    valor=int(valor)
    valor_binario.insert(0,novoValor)
    print()
print(valor_binario)
output=''.join(map(str, valor_binario))
print(output)#pode se usar print(''.join(map(str, valor_binario)))
print(valor)
print(cont)

