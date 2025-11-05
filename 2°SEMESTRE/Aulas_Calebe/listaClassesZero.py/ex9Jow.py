# Um racional ´e qualquer n´umero da forma p/q, sendo p inteiro e q inteiro n˜ao nulo. Crie
# uma classe para representar um racional e os seguinte m´etodos:
# 1
# (a) inverter sinal;
# (b) somar dois racionais;
# (c) subtrair dois racionais;
# (d) produto de dois racionais;
# (e) quociente de dois racionais;


class Racional:
    def __init__(self, p, q):
        self.p = p  
        self.q = q  
        if q == 0:
            print("Erro: o denominador não pode ser zero!")
            self.q = 1 
   
    def inverter_sinal(self):
        self.p = -self.p

   
    def somar(self, outro):
        novo_p = self.p * outro.q + outro.p * self.q
        novo_q = self.q * outro.q
        return Racional(novo_p, novo_q)

    
    def subtrair(self, outro):
        novo_p = self.p * outro.q - outro.p * self.q
        novo_q = self.q * outro.q
        return Racional(novo_p, novo_q)

   
    def multiplicar(self, outro):
        novo_p = self.p * outro.p
        novo_q = self.q * outro.q
        return Racional(novo_p, novo_q)

    
    def dividir(self, outro):
        novo_p = self.p * outro.q
        novo_q = self.q * outro.p
        return Racional(novo_p, novo_q)

    
    def mostrar(self):
        print(f"{self.p}/{self.q}")



print("=== CALCULADORA DE RACIONAIS (p/q) ===")

p1 = int(input("Digite o numerador do primeiro racional: "))
q1 = int(input("Digite o denominador do primeiro racional: "))
r1 = Racional(p1, q1)

p2 = int(input("\nDigite o numerador do segundo racional: "))
q2 = int(input("Digite o denominador do segundo racional: "))
r2 = Racional(p2, q2)

opcao = 0

while opcao != 6:
    print("\nEscolha uma operação:")
    print("1 - Inverter sinal do primeiro racional")
    print("2 - Somar")
    print("3 - Subtrair")
    print("4 - Multiplicar")
    print("5 - Dividir")
    print("6 - Sair")

    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        r1.inverter_sinal()
        print("Resultado:")
        r1.mostrar()

    elif opcao == 2:
        resultado = r1.somar(r2)
        print("Resultado da soma:")
        resultado.mostrar()

    elif opcao == 3:
        resultado = r1.subtrair(r2)
        print("Resultado da subtração:")
        resultado.mostrar()

    elif opcao == 4:
        resultado = r1.multiplicar(r2)
        print("Resultado da multiplicação:")
        resultado.mostrar()

    elif opcao == 5:
        resultado = r1.dividir(r2)
        print("Resultado da divisão:")
        resultado.mostrar()

    elif opcao == 6:
        print("Saindo...")

    else:
        print("Opção inválida!")
