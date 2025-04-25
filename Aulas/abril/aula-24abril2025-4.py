#desenvolva uma calculadora que solicita qual operação desejada (*, / , + , -) com comando para interronper, efetue o calciulo e imprima o resultado
while True:
    wish=input('Digite:\nM--para multiplicar\nD--para dividir\nA--para adição\nS--para subtração\nX--para sair\n').lower()
    if wish=='m':
        x=float(input('Digite o primeiro numero:'))
        y=float(input('Digite o segundo numero:'))
        z=x*y
        print(x,'*',y,'=','%.2f'%z)
    elif wish=='d':
        x=float(input('Digite o primeiro numero:'))
        y=float(input('Digite o segundo numero:'))
        z=x/y
        print(x,'/',y,'=','%.2f'%z)
    elif wish=='a':
        x=float(input('Digite o primeiro numero:'))
        y=float(input('Digite o segundo numero:'))
        z=x+y
        print(x,'+',y,'=','%.2f'%z)
    elif wish=='s':
        x=float(input('Digite o primeiro numero:'))
        y=float(input('Digite o segundo numero:'))
        z=x-y
        print(x,'-',y,'=','%.2f'%z)
    elif wish=='x':
        break