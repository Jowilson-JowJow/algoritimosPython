#faca um programa que peça uma nota, entre zero a dez. mostre uma mensagem caso o valor seja invalido e continue pedindo até que o usuario informe um valor válido
while True:
    nota=int(input('Digite uma nota de zero a dez:'))
    if 0<=nota<=10:
        print('nota é: ',nota)
        break
    else:
        print('digite de novo')