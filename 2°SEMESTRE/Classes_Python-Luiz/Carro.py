class Carro:
    def __init__(self, marca, modelo, cor, ano, valor, consumo):
        """Inicializa os atributos do carro"""
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.nivel = 0  
        self.consumo = consumo  

    def abastecer(self, quantidade):
        """Incrementa o nível do tanque de combustível"""
        self.nivel += quantidade
        print(f"Você abasteceu {quantidade} litros. Nível atual: {self.nivel:.2f} litros.")

    def andar(self, distancia):
        """Simula o carro andando e consome combustível"""
        combustivel_gasto = distancia * self.consumo
        if combustivel_gasto > self.nivel:
            print("Não há combustível suficiente para percorrer essa distância!")
        else:
            self.nivel -= combustivel_gasto
            print(f"O carro percorreu {distancia} km e gastou {combustivel_gasto:.2f} litros de combustível.")
            print(f"Nível de combustível restante: {self.nivel:.2f} litros.")

    def verificar_nivel(self):
        """Verifica o nível atual de combustível"""
        print(f"Nível atual de combustível: {self.nivel:.2f} litros.")

    def calcular_imposto(self):
        """Calcula o IPVA do carro (3,5% do valor do carro)"""
        ipva = self.valor * 0.035
        print(f"O valor do IPVA do carro é: R$ {ipva:.2f}")


def main():
    marca = input("Informe a marca do carro: ")
    modelo = input("Informe o modelo do carro: ")
    cor = input("Informe a cor do carro: ")
    ano = int(input("Informe o ano do carro: "))
    valor = float(input("Informe o valor do carro: R$ "))
    consumo = float(input("Informe o consumo do carro (litros por km): "))

    carro = Carro(marca, modelo, cor, ano, valor, consumo)

    while True:
        print("\nEscolha uma ação:")
        print("1 - Abastecer")
        print("2 - Andar")
        print("3 - Verificar nível de combustível")
        print("4 - Calcular IPVA")
        print("5 - Sair")
        
        escolha = input("Digite o número da ação: ")

        if escolha == "1":
            quantidade = float(input("Quantos litros deseja abastecer? "))
            carro.abastecer(quantidade)
        elif escolha == "2":
            distancia = float(input("Quantos quilômetros o carro percorreu? "))
            carro.andar(distancia)
        elif escolha == "3":
            carro.verificar_nivel()
        elif escolha == "4":
            carro.calcular_imposto()
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
