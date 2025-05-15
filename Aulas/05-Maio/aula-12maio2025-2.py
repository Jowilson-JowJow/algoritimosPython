#Numa eleição existem três candidatos. Faça um programa que peça o número total e eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato. Mostre também o Candidato campeão.
num_eleitores=int(input('Digite a quantidade de eleitores: '))
votos_1=0
votos_2=0
votos_3=0
for i in range(num_eleitores):
    x=input('digite: \n1--candidato João Honesto\n2--candidato Tiririca\n3--candidato ficha limpa')
    if x=='1':
        votos_1+=1
    elif x=='2':
        votos_2+=1
    elif x=='3':
        votos_3+=1
    else:
        print('voto invalido, vote de novo')
if votos_1>votos_2 and votos_1>votos_3:
    print('João honesto ganhou com: ',votos_1,'votos')
elif votos_2>votos_1 and votos_2>votos_3:
    print('Tiririca ganhou com: ',votos_2,'votos')
if votos_3>votos_1 and votos_3>votos_2:
    print('Fixa limpa ganhou com: ',votos_3,'votos')
