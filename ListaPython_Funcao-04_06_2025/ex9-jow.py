#Crie uma função que receba uma lista de nomes e retorne apenas os nomes com mais de 5 letras.
def vector():
    vector1=[]
    while True:
        try:
            x = input("entered\nx--to exit\nenter name: ")
            if x=='x' or x=='X':
                break
            else:
                vector1.append(x)
        except ValueError:
            print("Entered only x or name")
    print(f'the list is {vector1}')
    name_greater_5=[name for name in vector1 if len(name)>5 ]
    print('Names longer than 5 characters is', name_greater_5)

vector()