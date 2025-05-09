#Faça um programa que leia 5números e informe a soma e a média dos números. Sem usar usar sum, lista, len, etc... utlizando o for
#num1, num2, num3, num4, num5=map(int, input('Digite um numero: ').split())
nota = 0
x=int(input('digite a quantidade de notas para a média do aluno:'))
for i in range(x):
    nota+=int(input('Digite a nota do aluno: '))
print(nota)
print(nota/x)

#resposta do prof ederson
y=0
z=0
#t=int(input('digite o quantas avaliações foi feita: '))
#for i in range(t): eu que coloque a linha 13 e 14 no lugar da 15 
for i in range(5):
    print('Digite', i+1, "° valor")
    x=int(input())
    y=y+x
    z=z+1
print(z)
print(y)
print(y/z)
