#Faça um programa que imprima uma lista de times, adicionando um numeral.
#Ex.:
#Entrada:
#Time = [“Palmeiras”, “Flamengo”, “São Paulo”]
#Saída:
#1 – Palmeiras
#2 - Flamengo
#3 – São Paulo
times_br_2024 = ['athletico-pr', 'atletico-mg', 'bahia', 'botafogo', 'bragantino','corinthians', 'coritiba','cruzeiro', 'cuiaba',
'flamengo','fluminense', 'fortaleza', 'goias', 'gremio', 'internacional','palmeiras', 'santos', 'sao paulo', 'vasco', 'america-mg']
for i in range(len(times_br_2024)):
    print(i+1,'-',times_br_2024[i])
