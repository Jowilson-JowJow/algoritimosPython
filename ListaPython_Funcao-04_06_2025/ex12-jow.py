#Crie uma função que converta graus Celsius para Fahrenheit.
def f(c):
    f=(9/5)*c+32
    print(f'A temperatura de {c} °C corresponde a temperatura de {f} °F')

def c1(f1):
    c1=(5/9)*(f1-32)
    print(f'A temperatura de {f1} °F corresponde a temperatura de {c1} °C')

def k(c2):
    k=c2+273.15
    print(f'A temperatura de {c2} °C corresponde a temperatura de {k} K')

def c3(k1):
    c3=k1-273.15
    print(f'A temperatura de {k1} K corresponde a temperatura de {c3} °C')

def k2(f2):
    k2=(5/9)*(f2-32)+273.15
    print(f'A temperatura de {f2} °F corresponde a temperatura de {k2} K')

def f3(k3):
    f3=(9/5)*(k3-273.15)+32
    print(f'A temperatura de {k3} K corresponde a temperatura de {f3} °F')

while True:
    menu=input('Digite:\n"1"  °C-->°F\n"2"  °F-->C\n"3"  °C-->K\n"4" k-->°C\n"5" F-->K\n"6"  K-->F\n"x" to exit').lower()
    if menu=='1':
        x=float(input('Digite a temperatura em °C: '))
        f(x)
    elif menu=='2':
        x=float(input('Digite a temperatura em °F: '))
        c1(x)    
    elif menu=='3':
        x=float(input('Digite a temperatura em °C: '))
        k(x)
    elif menu=='4':
        x=float(input('Digite a temperatura em K: '))
        c3(x)
    elif menu=='5':
        x=float(input('Digite a temperatura em °F: '))
        k2(x)
    elif menu=='6':
        x=float(input('Digite a temperatura em K: '))
        f3(x)
    elif menu=='x':
        break

