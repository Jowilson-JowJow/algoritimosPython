#criar um codigo para ler o ano de nascimento e retornar se ele pode votar ou não
idade=int(input("Digite o ano de nascimento com os quatro digitos:"))
idadeVoto=2025-idade
if idadeVoto >=16 and idadeVoto<=70:
    print("parabens vc pode votar")
else:
    print("voce não pode votar.")
