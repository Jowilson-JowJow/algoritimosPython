#faça um programa que leia tres numeros e mostre o maior e o menor deles.
print('Digite tres numeros diferentes: \n')
num1=int(input())
num2=int(input())
num3=int(input())
print('Os numeros digitados foram:', num1, num2, num3)
if num1>num2 and num2>num3:
    print(num1,'é o maior numero digitado\n',num3,'é o menor numero digitado')
elif num1>num3 and num3>num2:
    print(num1,'é o maior numero digitado\n',num2,'é o menor numero digitado')
elif num2>num1 and num1>num3:
    print(num2,'é o maior numero digitado\n',num3,'é o menor numero digitado')
elif num2>num3 and num3>num1:
    print(num2,'é o maior numero digitado\n',num1,'é o menor numero digitado')
elif num3>num1 and num1>num2:
    print(num3,'é o maior numero digitado\n',num2,'é o menor numero digitado')
elif num3>num2 and num2>num1:
    print(num3,'é o maior numero digitado\n',num1,'é o menor numero digitado')
else:
    print('Você não digitou tres numeros diferentes!!!!')