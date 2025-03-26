#leia um numero e informe se ele é positivo, egativo ou zero
num=int(input("Digite um numero do conjunto dos numero inteiros"))
if num==0:
    print("O numero digitado é zero")
elif num<0:
    print("O numero é negativo")
elif num>0:
    print("O numero é positivo")