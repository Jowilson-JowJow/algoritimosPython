#faça um programa que receba um vetor de 5 numeros inteiros e mostre-os.
#mostre o maior deles
#mostre o menor deles
#mostre a quantidade de numeros
#some os numeros
lista=[]
lista.append(int(input("Digite um numero: ")))
lista.append(int(input("Digite um numero: ")))
lista.append(int(input("Digite um numero: ")))
lista.append(int(input("Digite um numero: ")))
lista.append(int(input("Digite um numero: ")))
print(lista)
print("O valor maximo é ",max(lista))
print("O valor minimo é ",min(lista))
print("A quantidade de numeros é ", len(lista))
print("a soma é ", sum(lista))