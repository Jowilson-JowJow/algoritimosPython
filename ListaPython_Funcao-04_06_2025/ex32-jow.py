#Crie uma função que retorne os números pares de uma lista usando list comprehension.

def lista_pares():
    pares=[]
    lista1()
    pares=[num for num in lista1 if num%2 == 0]
    print(f'Os numeros pares desta lista são: {pares}')

def lista1():
    lista=[]
    while True:
        menu=int(input('Digite:\n1 -- para iniciar a lista\n2 -- sair'))
        if menu == 1:
            while True:
                entrada=input('Digite um numero para acrescentar na lista (quando quiser parar só digitar x): ').lower()
                if entrada == 'x':
                    break
                try:
                    num=int(entrada) 
                    lista.append(num)
                except ValueError:
                    print('Por favor, digite um número válido ou "x" para sair.')
                else:
                    print('Digite um numero ou x')
        elif menu==2:
            break
        else:
            print("digite 1 ou 2")
    return lista


lista_pares()

