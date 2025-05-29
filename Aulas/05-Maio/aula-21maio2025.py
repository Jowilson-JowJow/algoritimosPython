#exercicios de tratamento de exceção. slide do exercicios no teams no dia 21 de maio de 2025
#é para fazer cadastro do cliente (nome, sobrenome, rg, cfp, endereço, fone, idade)
#é para fazer cadastro da passagem (destino, origem, duração, valor passagem, desconto 5%)
#é para fazer cadastro avião (modelo, ano, hoaras do voo, cor, quantidade de passageiros)
#é para fazer cadastro tripulação (nome, descrição cargo, idade, data de adimissão, fone)
# O Algoritmo deve ter a opção de cadastrar, imprimir relatórios e encerrar.
#Utilize todas as técnicas possíveis, while, for, try, etc...


#cadastro do cliente=cli
while True:
    lista_cli=[]
    cli_nome=input('Digite o Nome: ')
    cli_sobrenome=input('Digite o sobrenome: ')
    cli_rg=int(input('Digite o RG (apenas numeros): '))
    cli_cpf=int(input('Digite o CPF (apemas numeros): '))
    cli_rua=(input('Digite o nome da rua: '))
    cli_num=int(input('Digite o numero da residencia: '))
    cli_bairro=(input('Digite o bairro: '))
    cli_cidade=(input('Digite a cidade: '))
    cli_fone=int(input('Digite o fone (apemas numeros): '))
    cli_idade=int(input('Digite o idade (apemas numeros): '))
    lista_cli.extend([cli_nome,cli_sobrenome,cli_rg,cli_cpf,cli_rua,cli_num,cli_bairro, cli_cidade, cli_fone,cli_idade])
    print(lista_cli)
