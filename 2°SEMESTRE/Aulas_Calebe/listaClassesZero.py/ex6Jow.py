# Implemente uma classe para representar em vetor (x,y,z) no R3. Implemente os m´etodos
# para calcular a soma, subtrac¸ ˜ao, produto vetorial, produto escalar e m´odulo.


import math

class Vetor:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z =z
    

    def soma(self,outro):
        return Vetor(self.x+outro.x,self.y+outro.y,self.z+outro.z)
    
    def subtracao(self,outro):
        return Vetor(self.x-outro.x,self.y-outro.y,self.z-outro.z)

    def produto_escalar(self, outro):
        return Vetor(self.x*outro.x,self.y*outro.y,self.z*outro.z)
    
    def produto_vetorial(self, outro):
        return Vetor(self.y*outro.z-self.z*outro.y,self.z*outro.x-self.x*outro.z,self.x*outro.y-self.y*outro.x)
        
    def modulo(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
             


v1=Vetor(1,2,1)
v2=Vetor(2,0,-1)
v_soma=v1.soma(v2)
print(f"O vetor_A: ({v1.x}, {v1.y}, {v1.z})")
print(f"O vetor_B: ({v2.x}, {v2.y}, {v2.z})")
print(f"A soma Vetor_A + Vetor_B = : ({v_soma.x}, {v_soma.y}, {v_soma.z})")
v_subtracao = v1.subtracao(v2)
print(f"A subtração Vetor_A - Vetor_B = : ({v_subtracao.x}, {v_subtracao.y}, {v_subtracao.z})")
v_escalar=v1.produto_escalar(v2)
print(f"O produto escalar entre o Vetor_A e Vetor_B é= : {v_escalar.x+v_escalar.y+v_escalar.z }")
v_vetorial=v1.produto_vetorial(v2)
print(f"O produto vetorial entre o Vetor_A e Vetor_B é= : ({v_vetorial.x}, {v_vetorial.y}, {v_vetorial.z})")
v_modulo1=v1.modulo()
print(f"O módulo do vetor A é = {v_modulo1:.2f}")
v_modulo2=v2.modulo()
print(f"O módulo do vetor B é = {v_modulo2:.2f}")


