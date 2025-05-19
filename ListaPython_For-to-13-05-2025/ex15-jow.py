#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
fat=int(input('Digite o numero para fazer o fatorial:\n'))
resultado=1
for n in range(1,fat+1):
    resultado=resultado*n
print(f'o fatorial de ',fat, '! = ', resultado)
