#peça para o usuario informar a sua idade e verifique se ele tem idade para votar (entre 16 e 70 anos)
idade=int(input("digite a sua idade:"))
if idade>=16 and idade <=70:
    print("você  pode votar")
else:
    print("Você não pode voltar")
