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
    cli_end=int(input('Digite o endereço (apemas numeros): '))#separar em rua, bairro, numero cidade e cpe
    cli_fone=int(input('Digite o fone (apemas numeros): '))
    cli_idade=int(input('Digite o idade (apemas numeros): '))
    lista_cli.extend([cli_nome,cli_sobrenome,cli_rg,cli_cpf,cli_end,cli_fone,cli_idade])

