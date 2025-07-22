#Escreva uma função que receba um número e retorne a tabuada dele (de 1 a 10).
def table(num):
    for i in range (1,11):
        print(f'{num}x{i} = {num*i}')


x=int(input('Enter a number to see its multiplication table: '))
table(x)      
