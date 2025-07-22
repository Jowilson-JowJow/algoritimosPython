#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto 
# indeterminado de temperatura, bem como o mês e o ano que ocorreu essa temperatura, e informe ao final
# a menor e a maior temperaturas informadas, o mês e o ano em que elas ocorrera, bem como a média de todas
# as temperaturas.
maior = -99999999999999999
menor=99999999999999999
soma=0
dados=int(input('Digite quantos dados de temperatura será informado:'))
for i in  range(dados):
    temp=float(input('Digite a temperatura:'))
    mes=input('Digite o mês da medição (ex: jan. fev, ...):')
    ano=int(input('Digite o ano (no formato aaaa) dessa medida:'))
    if maior <temp:
        maior=temp
        maiormes=mes
        maiorano=ano
    if menor>temp:
        menor=temp
        menormes=mes
        menorano=ano
    soma=soma+temp
media = soma/dados
print(f'A maior temperatura foi de {maior}°\no mês e o ano correspondente foram: {maiormes},{maiorano}')
print(f'A menor temperatura foi de {menor}°\no mês e o ano correspondente foram: {menormes},{menorano}')
print('A média das temperatura foi de %.2f'%media)