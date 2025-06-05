#Escreva uma função que receba uma lista de números e retorne o maior elemento.
def vector():
    vector1=[]
    while True:
        try:
            x = input("entered\nx--to exit\nenter number: ")
            if x=='x' or x=='X':
                break
            else:
                x=int(x)
                vector1.append(x)
        except ValueError:
            print("Entered only x or number")
    print(f'the list is {vector1}')
    print('the max on the list is', max(vector1))

vector()