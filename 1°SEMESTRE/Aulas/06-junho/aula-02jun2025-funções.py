#estudar a sintaxe da função: exemplo
#deve composta por "def"+"nome"+":" indentação onde se coloca os comandos;
#==========================================================
# def hello():
#     print('ola!!!')
# hello()
#==========================================================
# def hello(nome):
#     print('ola!!!',nome)
# hello("jowjow")
#==========================================================
# def hello(nome):
#     print('ola!!!',nome)
# a=input("nome: ")
# hello(a)
#==========================================================
# def hello(nome, idade):
#     print(f'Olá {nome}\nSua idade é: {idade}')

# hello("jowjow",24)
#==========================================================
# def farh_to_cel(temp):
#     return ((temp - 32)*(5/9))

# print(farh_to_cel(68) - farh_to_cel(50))
#==========================================================
# def calcular_pagamento(qtd_horas,valor_hora):
#     horas=float(qtd_horas)
#     taxa=float(valor_hora)
#     if horas<=40:
#         salario=horas*taxa
#     else:
#         h_excd=horas-40
#         salario=40*taxa+(h_excd*1.5*taxa)
#     print(salario)

# calcular_pagamento(38,20)
#==========================================================
# def calcular_pagamento():
#     horas=float(input('digite a suas horas trabalhadas: '))
#     taxa=float(input('digite o valor da hora trabalhada: '))
#     if horas<=40:
#         salario=horas*taxa
#     else:
#         h_excd=horas-40
#         salario=40*taxa+(h_excd*1.5*taxa)
#     print(salario)

# calcular_pagamento()
#==========================================================
# def soma(x,y):
#     result=x+y
#     return result

# a=int(input("1° numero: "))
# b=int(input("2° numero: "))
# res=soma(a,b)
# print("soma:",res)
#==========================================================
def cadastro():
    nome=input("nome: ")
    idade=input("idade: ")
    return nome, idade

print("Iniciando cadastro...")
nome, idade = cadastro()
print("Cadastro realizado com sucesso: ")
print (f"Seu nome é {nome} e vc tem {idade}, anos de idade.")