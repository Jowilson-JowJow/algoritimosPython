#Faça um programa que leia 5 números e informe a soma e a média dos números.
#Sem usar usar sum, lista, len, etc...
nota = 0
x=int(input('digite a quantidade de notas para a média do aluno:'))
for i in range(x):
    nota+=int(input('Digite a nota do aluno: '))
print(nota)
print(nota/x)