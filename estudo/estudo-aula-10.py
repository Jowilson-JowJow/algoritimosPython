# em python os objetossão classificados em classes e tipos de dados diferentes.
# 5 é inteiro e "Ola Mudo!" é um texto - string
# para identificar uma string é tudo que esta entre aspas.
print("\nOlá Mundo.")#funciona com ""
print('Olá Mundo.')#funciona com ''
print(2+3); #com ponto e virgula no final ele retorna o valor da somaa -- 5
print(2+4,"\n") #sem o ponto e virgula no final ele tambem retorna a soma --6
#--------------------------------------
#o \n dentro das "" na função string serve par apular linha e sendo chamada de caractere de escape
#por causa disso para por uma barra invertida como texto em um string deve se usar duas barras \\
print("2\n3")#nesse caso retorna 2 pula linah 3
print("2\\3")#retorna o valor 2\3
print("2//3")#nesse caso retorna 2//3 pos a barra / não é caractere de escape
print("2/3")#nesse caso retorna 2/3 pois a barra / não é caractere de escape
#---------------------------------------
#por padrão a função print() tem dois argumentos de palavras chaves. Quia são esses 2 argumentos?
# por padrão sempre que vc usar a função print() o ultimo caractere sera a quebra de pagina ou seja \n
# já o parametro end=""  cancela esse ultimo argumento e junta os print()
print("Ola eu me chamo")#retorna apenas essa string e pula a linha para a proxia string
print("Jowilson")#retorna apenas essa string e pula a linha apara a proxima string
print("Ola eu me chamo ",end="")#retorna a string e junta sem espaços pois as "" esta vazia em end="" juntando a strihg de baixo com essa string
print("Jowilson")#será juntada com a string de cima por causa da função end=""
print("Ola eu me chamo ",end="prof.")# reotna a string e junta com a de baixo porem separa as duas strings pelo caracter colocado entre as ""
print("Jowilson")
#------------------------------------------
#sempre que no print() se usa virgula para separar as strings, por padrão a virgula dara um espaço entre as strings
print("carlos","joão","tem 15 anos","cada") #retona "carlos joão tem 15 nos cada"
#para mudar o caractere de separação usa-se a função sep="" nesse caso o que tiver entre as aspas será o caractere de separação
print("carlos","joão","tem 15 anos","cada",sep="--")#retorna "carlos--joão--tem 15 anos--cada"
print("carlos","joão","tem 15 anos","cada",sep="-*-")#retorna "carlos-*-joão-*-tem 15 anos-*-cada"
#-----------------------------------------------
#todo numero poser inteiro ai deve-se informar que é int mas se for com ponto decimal, não pode uar virgula nesse caso o numero sera float (ponto flutuante ou floating point)
print(3.14)#retorna 3.14
print(type(3.14))#retorna o tipo de objeto, nesse caso retorna float por ser um numero com ponto decimal
print(type(2+3))#retorna o tipo do objeto como sendo inteiro-int
print(type("2+3"))#retorna o tipo de objeto como sendo string-str
#----------------------------------------------------
# toda string pode ser delimitada por 'casa' ou "casa" ou '''casa''' ou """casa"""
print(type('casa'))#retorna uma string
print(type('''casa'''))#retorna uma string
print(type("casa"))#retorna uma string
print(type("""casa"""))#retorna uma string
#---------------------------------------------
#para o valores booleanos existe o True e o False
#no casso, os operadores são: soma(+), subtração(-), multiplicação(*), divisão(/). deve se respeita as ordem nas {[()]}
print(3*3)#retorna multiplicação
print(3+3)#retorna soma
print(3-3)#retorna subtração
print(3/3)#retorna divisão
print(3**3)#retorna potenciação
print(5%3)# retorna o resto da divisão nesse caso 2
print(11//2)#retorna o valor inteiro da divisão nesse caso 5
#----------------------------------------------
#Comandos de atribuição(asignment statement) cria variavel e atribui valor a ela
mensagen="ola, continue assim, estude bastante."
n=1977
pi=3.1416
#não confundir o sinal de atribuição (=) co o sinal de igual (==)
print(type(mensagen))
print(mensagen)
print(type(n))
print(n)
print(type(pi))
print(pi)
#-------------------------------------
#veja para fazer a rais quadrada usa-se a forma de x^1/2
num=int(input("digite o numero para extrair as raizes:\n"))
raizQuadrada=num**(1/2)
raizCubica=num**(1/3)
raisQuintupla=num**(1/5)
print(raizQuadrada,raizCubica, raisQuintupla, sep=("--"))
#não pode esquecer de atribuir ao numero se ele é inteiro ou float 
#por que se não retorna erro pois ele considera string e ai não faz contas
n=25#dessa forma ja é considerado como numero e não texto, o reconhecimento é altomatico
n=n**(1/2)
print(n)
#--------------------------------------------------
#para fazer um comentario em bloco de linha pode colocar ''' antes e ''' depois 
'''num=int(input("digite o numero para extrair as raizes:\n"))
raizQuadrada=num**(1/2)
raizCubica=num**(1/3)
raisQuintupla=num**(1/5)
print(raizQuadrada,raizCubica, raisQuintupla, sep=("--"))'''
#tenho minhas duvidas
#------------------------------------------
#escreva um codigo que calcule o imc
peso=(int(input("digite a sua massa: ")))
altura=(float(input("digite a sua altura")))
imc=peso/altura**2
print(imc)
print("%.2f"%imc)
