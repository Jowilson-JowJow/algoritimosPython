##Faça um programa que imprima uma lista de times,adicionando um nnumeral.
#Ex.:
#Entrada: Time=["Palmeiras", "Flamengo", "SãoPaulo"] 
#Saída: 
#1- Palmeiras 
#2-Flamengo 
#3-SãoPaulo
time=['Palmeiras','Flamengo','São Paulo']
for x in range(len(time)):
    print(f'{x+1} - {time[x]}')

#ou dessa forma

for i, time in enumerate(time, start=1):
    print(f"{i} - {time}")
