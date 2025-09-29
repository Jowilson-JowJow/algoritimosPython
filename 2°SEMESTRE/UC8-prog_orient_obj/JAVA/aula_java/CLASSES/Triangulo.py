class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura=altura

    def calcular_area(self) ->float:
        area = (self.base*self.altura)/2
        return area
    
t1 = Triangulo(9,15)
t2 = Triangulo(4.5,6)

print("Base do T2: ",t2.base)
print(t2.calcular_area())

