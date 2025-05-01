#simular uma urna eletronica. 1,2,3,4 qualquer outro numero é voto nulo voto nulo e se não digitar nada e dar entere é voto em branco / 0 finaliza o programa e ai imprima apenas quem teve maior numero de votos
cand1=0
cand2=0
cand3=0
cand4=0
branco=0
nulo=0
while True:
    voto=int(input('A votação iniciou: \nDigite 1 -- para o candidato João Canabrava\nDigite 2 -- para a candidata florentina de jesus\nDigite 3 -- para o candidato Jhon Rambo\nDigite 4 -- para a candidata mãe do stifler\n'))
    if voto==1:
        cand1 +=1
    elif voto==2:
        cand2 +=1
    elif voto==3:
        cand3 +=1
    elif voto==4:
        cand4 +=1
    elif voto=="":
        branco +=1
    elif voto==0:
        break
    else:
        nulo+=1
if cand1>cand2 and cand1>cand3 and cand1>cand4:
    print('O candidato João Canabrava é o vencedor com: ', cand1, 'votos')
elif cand2>cand1 and cand2>cand3 and cand2>cand4:
    print('O candidato florentina de jusus é o vencedor com: ', cand2, 'votos')
elif cand3>cand1 and cand3>cand2 and cand3>cand4:
    print('O candidato jhon rambo é o vencedor com: ', cand3, 'votos')
elif cand4>cand1 and cand4>cand2 and cand4>cand3:
    print('O candidato mae do stifler de jusus é o vencedor com: ', cand4, 'votos')