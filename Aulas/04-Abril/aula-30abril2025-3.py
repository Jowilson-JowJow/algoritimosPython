#exercicio do estaoque os detalhes da execusão do codigo esta no teams 
cod10=int(input('Quantidade de caderno no estoque: '))
cod20=int(input('Quantidade de caneta no estoque: '))
cod30=int(input('Quantidade de lápis no estoque: '))
cod40=int(input('Quantidade de borracha no estoque: '))
cod50=int(input('Quantidade de régua no estoque: '))

while True:
    x=input('Digite:\nE - entrada de estoque: \nS - saída de estoque: \nR - Relatório: \nX - sair:\n').lower()
    if x=='e':
        caderno=int(input('entrada de caderno: '))
        cod10=cod10+caderno
        caneta=int(input('entrada de caneta: '))
        cod20=cod20+caneta
        lapis=int(input('entrada de lapis: '))
        cod30=cod30+lapis
        borracha=int(input('entrada de borracha: '))
        cod40=cod40+borracha
        regua=int(input('entrada de regua: '))
        cod50=cod50+regua
    elif x=='s':
        caderno=int(input('saida de caderno: '))
        cod10=cod10-caderno
        caneta=int(input('saida de caneta: '))
        cod20=cod20-caneta
        lapis=int(input('saida de lapis: '))
        cod30=cod30-lapis
        borracha=int(input('saida de borracha: '))
        cod40=cod40-borracha
        regua=int(input('saida de regua: '))
        cod50=cod50-regua
    elif x=='r':
        print('RELATÓRIO:')
        print('Quantidade de caderno no estoque: ',cod10)
        print('Quantidade de caneta no estoque: ',cod20)
        print('Quantidade de lapis no estoque: ',cod30)
        print('Quantidade de borracha no estoque: ',cod40)
        print('Quantidade de regua no estoque: ',cod50)
    elif x=='x':
        break




