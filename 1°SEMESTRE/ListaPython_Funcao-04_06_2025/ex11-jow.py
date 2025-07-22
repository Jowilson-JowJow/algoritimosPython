#Crie uma função que receba um número e retorne uma lista com todos os divisores dele.
def dividers(x):
    vector=[]
    for i in range(1,x+1):
        num=x%i
        if num==0:
            vector.append(i)
    return vector


while True:
    try:
        number=int(input('enter the number:')) 
        result=dividers(number)
        print(f'divisors of {number} is {result}')
        break
    except ValueError:
        print ('enter the number!!!')

