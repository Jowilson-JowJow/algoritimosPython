#Crie uma função que receba uma lista e retorne a média dos elementos.
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
    print('the average on the list is', sum(vector1)/(len(vector1)))

vector()