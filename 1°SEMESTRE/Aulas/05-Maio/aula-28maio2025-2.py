#atividade teams eu e o gravaena
nome=[]
idade=[]
sexo=[]
cpf=[]
endereco=[]
cidade=[]
estado=[]

while True:
    try:
        nomes=input('digite o nome: ')
        idades=int(input('digite a sua idade: '))
        sexos=input('digite o sexo: ')
        cpfs=int(input('Digite o CPF: '))
        enderecos=input('digite o endereço: ')
        cidades=input('digite a cidade: ')
        estados=input('digite o estado: ')
    except:
        print('coloque a idade certa!')
    endereco.append(enderecos)
    cpf.append(cpfs)
    cidade.append(cidades)
    estado.append(estados)
    idade.append(idades)
    nome.append(nomes)
    sexo.append(sexos)
    with open('cadastro.txt','a',encoding="utf-8") as x:
        x.write(f'Nome:{nome[-1]},Idade:{idade[-1]},Sexo:{sexo[-1]},CPF:{cpf[-1]},Endereço:{endereco[-1]},Cidade:{cidade[-1]},Estado:{estado[-1]}\n---------------------------------------------------------------------------------\n')
    novo=input('Você deseja fazer um novo cadastro: S/N').lower()
    if novo=='s':
        print('novo cadastro')
    elif novo=='n':
        print('cadastro encerrados.')
        break
    else:
        print('digite S ou N')

pesq=input('Você deseja pesquisar um cadastro: S/N').lower()
if pesq=='s':
    y=input('Digite o CPF: ')
elif novo=='n':
    print('pesquisa encerrados.')
else:
    print('digite S ou N')

with open('cadastro.txt','r')as f:
    for linha in f:
        if y in linha.lower():
            print(linha)


