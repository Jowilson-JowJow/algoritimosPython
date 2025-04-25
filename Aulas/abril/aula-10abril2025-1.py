#faça um programa que verifique se a letra digitada é F, M ou O. conforma a letra escrever: F-feminino, M masculino, O -outros ou sexo invalido
sexo=input('Digite o seu genero "F", "M", ou "O"').upper()
if sexo=='F':
    print('F-Feminino')
elif sexo=='M':
    print('M-Masculino')
elif sexo=='O':
    print('O- Outros')
else:
    print('Sexo Invalido')
