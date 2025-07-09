#Crie uma função que simule uma calculadora simples (operações: +, -, *, /), com três parâmetros: número 1, número 2 e operação.
def menu(x,y):

    escolha=int(input('Digite:\n1 -- somar\n2 -- subtrair\n3 -- multiplicar\n4 -- dividir\n5 -- sair'))
    if escolha==1:
        soma=x+y
        print(f'a soma entre {x} e {y} é igual é {soma:.2f}')
    elif escolha==2:
        subtracao=x-y
        print(f'a subtação entre {x} e {y} é igual é {subtracao:.2f}')
    elif escolha==3:
        multiplicacao=x*y
        print(f'a multiplacação entre {x} e {y} é igual é {multiplicacao:.2f}')
    elif escolha==4:
        divisao=x/y
        print(f'a subtação entre {x} e {y} é igual é {divisao:.2f}')
    else:
        print('Digite 1 ou 2 ou 3 ou 4')


def cal():
    while True:
        operacao=int(input("Digite:\n1 -- calculadora\n2 -- sair"))
        if operacao==1:
            num1=float(input('Digite o primeiro numero para se calcular'))
            num2=float(input('Digite o segundo numero para se calcular'))
            menu(num1,num2)
        elif operacao==2:
            break
        else:
            print('Digete 1 ou 2')

cal()