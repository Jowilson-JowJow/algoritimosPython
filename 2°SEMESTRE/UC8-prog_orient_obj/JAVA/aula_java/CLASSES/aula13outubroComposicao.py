import random

class Motor:
    def __init__(self, pot, comb):
        self.chassis = random.randrange(0,1000)
        self.potencia = pot
        self.combustivel = comb

    def get_combustivel(self):
        return self.combustivel


class Carro:
    def __init__(self, modelo, potencia_motor, combustivel):
        self.modelo = modelo
        self.motor = Motor(potencia_motor, combustivel)  # Composição


carro = Carro("Fusca", 1300, "Gasolina")

print(f"O {carro.modelo} possui motor {carro.motor.potencia} cilindradas")
print(f"O {carro.modelo} deve usar {carro.motor.get_combustivel()}")
del carro
