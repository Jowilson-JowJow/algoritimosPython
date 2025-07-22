#Crie uma função que retorne o menor valor entre três números.
def menor(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(f'this is th esmallst number entered {num1}')
    elif num2>num1 and num2>num3:
        print(f'this is th esmallst number entered {num2}')
    elif num3>num2 and num3>num1:
        print(f'this is th esmallst number entered {num3}')
    elif num1==num2 and num1==num3:
        print(num1)
    else:
        print('entered a number')



x=int(input('entered a number: '))
y=int(input('entered a number: '))
z=int(input('entered a number: '))
menor(x,y,z)