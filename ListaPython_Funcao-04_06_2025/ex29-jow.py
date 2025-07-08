#Crie uma função recursiva que calcule o n-ésimo número da sequência de Fibonacci.

def fibonacci(n):
    if n<=0:
        return "posição invalida"
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
num=int(input('Digite o numero de termos para a sequencia de fibonancci: '))
print(f'o {num}-ésimo numero da sequecia de fibonacci é: {fibonacci(num)}')