#faça um programa que leiA e valide as seguintes informações: NOME: maior ou igual a 3 caracteres; idade: entre 0 e 150; salario: maior que zero; sexo: 'f' ou 'm' ou 'o'; estado civile: 's' , 'c' , 'v' , 'd'
while True:
    nome= input('Digite seu nome: ')
    idade= int(input('Digite sua idade: '))
    salario= float(input('Digite seu salario: '))
    sexo= input('Digite seu nome: ')
    nome= input('Digite seu nome: ')
    #peguei pelo chat pra ver como é 
    # Validação do nome
while True:
    nome = input("Digite o nome (mínimo 3 caracteres): ")
    if len(nome) >= 3:
        break
    else:
        print("Nome inválido. Deve ter pelo menos 3 caracteres.")

# Validação da idade
while True:
    try:
        idade = int(input("Digite a idade (entre 0 e 150): "))
        if 0 <= idade <= 150:
            break
        else:
            print("Idade inválida. Digite um número entre 0 e 150.")
    except ValueError:
        print("Por favor, digite um número válido.")

# Validação do salário
while True:
    try:
        salario = float(input("Digite o salário (maior que 0): "))
        if salario > 0:
            break
        else:
            print("Salário inválido. Deve ser maior que zero.")
    except ValueError:
        print("Por favor, digite um número válido.")

# Validação do sexo
while True:
    sexo = input("Digite o sexo ('f' - feminino, 'm' - masculino, 'o' - outro): ").lower()
    if sexo in ['f', 'm', 'o']:
        break
    else:
        print("Sexo inválido. Use 'f', 'm' ou 'o'.")

# Validação do estado civil
while True:
    estado_civil = input("Digite o estado civil ('s' - solteiro, 'c' - casado, 'v' - viúvo, 'd' - divorciado): ").lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    else:
        print("Estado civil inválido. Use 's', 'c', 'v' ou 'd'.")

# Saída final com os dados validados
print("\n✅ Cadastro realizado com sucesso!")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R$ {salario:.2f}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")
