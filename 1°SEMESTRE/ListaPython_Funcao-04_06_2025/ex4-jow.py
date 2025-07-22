#4.	Escreva uma função que verifique se um número é par.
def even_number(x):
    if x%2==0:
        print('The number entered is a even number!')#o numero digitado é um numero par
    else:
        print("The number entered is an odd number!")#o numero digitado é um numero impar

a=int(input("enter a number: "))
even_number(a)