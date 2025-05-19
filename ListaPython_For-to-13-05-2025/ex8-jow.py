#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
#  turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
#Imprimir a média
n=int(input('Digite a quantidade de pessoas a ser cadastrada: '))
x=0
for i in range(n):
    i+=1
    idade=int(input('Digite a idade: '))
    x=x+idade
media=x/i
if media<=25:
    print('A quantidade de pessoas digitadas foi de: ',i,'pessoas')
    print('a Soma das idades da turma é ', x, 'e a média da turma é: ', media)
    print("a turma é jovem")
elif media<=60:
    print('A quantidade de pessoas digitadas foi de: ',i,'pessoas')
    print('a Soma das idades da turma é ', x, 'e a média da turma é: ', media)
    print('a turma é adulta')
else:
    print('A quantidade de pessoas digitadas foi de: ',i,'pessoas')
    print('a Soma das idades da turma é ', x, 'e a média da turma é: ', media)
    print('a turma é idosa')  