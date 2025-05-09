#faça um progarma que, dado um conjunto de N numeros, determine o menor valor, o maior valor e a soma dos valores. utilize o for (não pode usar: sum, média nem nada--na unha)
num=int(input('Digite quantos numeros tem o conjunto: '))
x=0
for i in range(num):
    print('Digite',i+1,'° numero')
    x=int(input())
print(x, end=' ')