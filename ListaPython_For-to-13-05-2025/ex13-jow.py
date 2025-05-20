#Faça um programa que peça 10 números inteiros, calcule (#o que é pra calcular?) e mostre a quantidade de números pares e a quantidade de
# números impares.
impar=0
par=0
for i in range(1,11):
    x=int(input(f'{i}° numero - '))
    if x%2==0:
        impar+=1
    elif x%2==1:
        par+=1
print(f'tem {par} numeros pares e {impar} numeros impares digitad')       
        
