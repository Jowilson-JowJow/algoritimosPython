#Um jogo consiste em lançar 6 vezes um dado cúbico, cujas faces são numeradas de 1 a 6, cada uma com a mesma probabilidade de ocorrer. Um jogador é considerado vencedor se obliver pelo menos 4 resullados pares. A probabilidade de um jogador vencer é:
#a resposta é a)73/64  b)11/32  c)15/64  d)73/32 

#como fazer função?
def fat (pos):
    resultado=1
    for n in range(1,pos+1):
        resultado=resultado*n
    return resultado

def comb(n,p):
    return fat(n)/(fat(p)*fat(n-p))

def prob(p,n):
    return p/n

def prob_comn(n, k, p):
    return comb(n,k)*(p**k)*((1-p)**(n-k))

#p(k)=c0mb(n,k)*p^k*(1-p)^n-k
caso1=comb(6,4)*(prob(3,6)**4)*(prob(3,6)**2)
print(caso1)
caso2=comb(6,5)*(prob(3,6)**5)*(prob(3,6)**1)
print(caso2)
caso3=comb(6,6)*(prob(3,6)**6)*(prob(3,6)**0)
print(caso3)
print('resultado: ',(caso1+caso2+caso3))

resp=prob_comn(6,4,prob(3,6))+prob_comn(6,5,prob(3,6))+prob_comn(6,6,prob(3,6))
print(resp)
#testar para varias situações