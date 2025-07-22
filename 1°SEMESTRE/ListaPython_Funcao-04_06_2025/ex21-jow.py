#Crie uma função que receba uma lista de números e retorne uma nova lista com os números elevados ao quadrado.
def vector():
    vector1=[]
    while True:
        try:
            x = input("==Entered==\nEnter a number (or x to exite): ")
            if x=='x' or x=='X':
                break
            else:
                x=int(x)
                vector1.append(x)
        except ValueError:
            print("Entered only x or number")
    print(f'the list is {vector1}')
    quadrado=[x**2 for x in vector1]
    print(quadrado)

vector()