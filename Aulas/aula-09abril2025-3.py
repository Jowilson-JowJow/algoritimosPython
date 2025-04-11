#Faça um algoritimo em python que receba duas notas e calcule a média aritmética e mostre o resultadoo. aprovado>=7 Reprovado<7
nota1=int(input('Digite a nota N1 do aluno: '))
nota2=int(input('Digite a nota N2 do aluno: '))
media=(nota1+nota2)/2
if (media>=7):
    print('Aprovado\nSua média é %.24f'%media)
else:
    print('Reprovado\nSua média é %.24f'%media)