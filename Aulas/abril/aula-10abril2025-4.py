#faça um programa que pergunte o preço de tres pordutos e informe qual você deve comprar sabendo que a decisão é sempre pelo mais barato
print('Digite tres preços de maeracorias: ')
num1=int(input())
num2=int(input())
num3=int(input())
print('Os numeros digitados foram:', num1, num2, num3)
if num1>num2 and num2>num3:
    print(num3,'compre esse produto')
elif num1>num3 and num3>num2:
    print(num2,'compre esse produto')
elif num2>num1 and num1>num3:
    print(num3,'compre esse produto')
elif num2>num3 and num3>num1:
    print(num1,'compre esse produto')
elif num3>num1 and num1>num2:
    print(num2,'compre esse produto')
elif num3>num2 and num2>num1:
    print(num1,'compre esse produto')
elif num3==num2 and num2>num1:
    print(num1,'compre esse produto')
elif num1==num2 and num2>num3:
    print(num3,'compre esse produto')
elif num1==num3 and num3>num2:
    print(num2,'compre esse produto')
else:
    print('todos tem o mesmo preço compre o que mais gostou')