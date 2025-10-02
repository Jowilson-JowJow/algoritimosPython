class Calculadora:
    pass
    def calcular(self, opcao, num1, num2):
        if opcao =='+':
            return self.__adicionar(num1,num2)
        elif opcao == '-':
            return self.__subtrair(num1,num1)
        else:
            print("opção Invalida")
    
    def __adicionar(self,n1,n2):#metodo privado
        return n1+n2
    
    def __subtrair(self,n1,n2):#metodo privado
        return n1-n2
    
calc = Calculadora()
result = calc.calcular('+',7,8)
print(result)
