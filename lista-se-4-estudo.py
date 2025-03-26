#criar um codigo para comprar maçãs a R$0,30 mas se comprar acima de uma duzia a maçã custará R$0,25 e retorne o valor da compra
precoMaca=0.30
precoDesconto=0.25
compra=int(input("Digite a qauntidade de mação compradas:"))
if compra>=12:
    print("O valor a ser pago é de R$ ",precoDesconto*compra)
else:
    print("O valor a ser pago é de R$ ",precoMaca*compra)
