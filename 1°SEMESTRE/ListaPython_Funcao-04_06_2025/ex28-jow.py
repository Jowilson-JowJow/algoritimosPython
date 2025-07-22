#Crie uma função recursiva para calcular o fatorial de um número.
#def fat(x):

def fat (num):
    y=1
    for i in range (1,num+1):
        y*=i
    print (y)

num=int(input('digite o numero: '))
fat(num)