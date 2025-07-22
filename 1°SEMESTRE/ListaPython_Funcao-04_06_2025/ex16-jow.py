#Crie uma função que gere uma lista com os n primeiros números pares.
def vector():
    while True:
        x=input('==Entered==\nEnter a number (or x to exit): ')
        if x.lower() =='x':
            break
        try:
            y=int(x)
            vector1=[]
            num=2
            while len(vector1)<y:
                vector1.append(num)
                num+=2
            print('The list with the first {x} even numbers is:', vector1)

        except ValueError:
            print("Invalid input! Enter only a number or 'x' to exit.")
     

vector()




