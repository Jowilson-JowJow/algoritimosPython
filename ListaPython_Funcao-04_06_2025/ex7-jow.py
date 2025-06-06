#Crie uma função que receba um número e retorne True se ele for primo.
def prime_number(x):
    if x<=1:
        print('The number entered is NOT a prime number')
        return
    for i in range(2,x):
        if x%i==0:
            print('The number entered is a NOT a prime number')
            return
    print('The number entered is a prime number')



a=int(input('enter de number you want to see if it is a oprime number: '))
prime_number(a)    