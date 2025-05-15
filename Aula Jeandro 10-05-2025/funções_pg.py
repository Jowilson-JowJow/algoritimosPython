#faça as definições para as formulas da PG
import time
import math
def pg_an(a1,q,n):
    result=a1
    # inicio = time.time()
    result=a1*q**(n-1)
    # fim=time.time()
    # tempo= fim-inicio
    # print(f'o tempo gasto foi de {tempo} segundos')
    return result

def n_pg(a1,q,result):
    n=(math.log(result/a1,10)/(math.log(q,10)))+1
    return n

def soma_pg(a1, q, n):
    return (a1*(1-q**n))/(1-q)

def pg(a1,q,n):
    termos=a1
    for i in range(a1,n):
        termos*=q
        print(termos)
    

def soma_pg_inf(a1,q):
    return (a1/(a1-q))

def produtos(a1, q ,n):
    return ((a1**n)*q((n*(n-1))/2))
    
#exercicio 1
print(pg_an(2,2,10))
#exercicio 2
print(n_pg(1,2,512))
#exercicio 3
print(pg_an(1,-3,-3))
#exercico 4 ta errado
print(n_pg(100,2,3200)*20)
