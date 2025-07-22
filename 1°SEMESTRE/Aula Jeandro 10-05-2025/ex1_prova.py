# Uma empresa possui 12 funcionários: 5 do setor vermelho, 4 do setor azul e 3 do setor verde. A diretoria quer 
# formar um comitê de 6 pessoas, sem repetir membros de setor (ou seja, ninguém de um setor pode estar
# mais de uma vez no comitê). O comitå deve ter.
# • Exatamente 2 pessoas do setor vermelho,
# • Exatamente 2 pessoas do setor azul,
# ◦ Exatamente 2 pessoas do setor verde.
# No entanto, há uma restrição adicional: dois funcionários do setor azul, João e Maria, não podem participar
# do comitê juntos (ou seja, ou entra João, ou entra Maria, ou nenhum dos dois, mas nunca os dois ao mesmo tempo).
# Pergunta:
# Qual é a probabilidade de se formar um comitổ válido (com a dlvisão 2-2-2 entre OS setores) sem que
# João e Maria estejam juntos, ao se escolher aleatoriamente um comitê de 6 pessoas respeitando a divisão dos setores?
# Dica para a resolução:
# 1. Calcule o numero total de comitės possiveis com 2 de cada setor (sem considerar Jodo e Mara),
# 2. Calcule quantos desses comitès Incluem tanto João quanto Marla.
# 3. Subtraia esse valor do total para encontrar os comitès válidos,
# 4. Divida o número de comitês válidos pelo total para obter a probabilidade.

def fat (pos):
    resultado=1
    for n in range(1,pos+1):
        resultado=resultado*n
    return resultado

def comb(n,p):
    return  fat(n)/(fat(p)*fat(n-p))

total=comb(5,2)*comb(4,2)*comb(3,2)
totalJeM=comb(5,2)*comb(3,2)
resp=((total-totalJeM)/total)*100
print('%.2f'%resp,'%')


