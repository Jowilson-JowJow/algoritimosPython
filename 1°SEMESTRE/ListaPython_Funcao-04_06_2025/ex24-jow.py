#Crie uma função que substitua todas as vogais de uma string por "*".
def substituir(frase,x,y):
    subst_letra=frase.replace(x,y)
    print(f'A frase digitada foi "{frase}"\ntrocando todas as letras "{x}" da frase por "{y}"\na frase será escrita dessa forma "{subst_letra}"')

fr=input('Digite uma frase: ')
letra=input('Digite a letra que você quer substituir nessa frase: ')
subst=input('Digite a nova letra ou caractere: ')
substituir(fr,letra,subst)


