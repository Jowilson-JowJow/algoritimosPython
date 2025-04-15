nota1=float(input('Digite a N1 do aluno:'))
nota2=float(input('Digite a N2 do aluno:'))
print('As notas digitadas foram: ', nota1,'e', nota2)
media=(nota1+nota2)/2
if (media>=7 and media<10):
    print('APROVADO')
elif(media<7):
    print('REPROVADO')
elif(media == 10):
    print('APROVADO COM DISTINÇÃO')
else:
    print('As notas digitadas estão erradas')
