#escreva um codigo que verifique a senha retornando acesso permitido ou acesso negado, a senha valida é 1234
senhaCerta=1234
senha=int(input("Digite a senha:"))
if senhaCerta==senha:
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")
