#faça um programa que leia um nome de usuario e a senha e não aceite a senha igual ao nome do usuario, mostrando uma mensagem de erro e voltando a pedir as informações.
while True:
    nome=input('Digite o nome: ').lower()
    senha=input('Digite a senha: ').lower()
    print(nome.lower())
    print(senha.lower())
    if senha==nome:
        print('ERRO')
    else:
        print('OK')
        break