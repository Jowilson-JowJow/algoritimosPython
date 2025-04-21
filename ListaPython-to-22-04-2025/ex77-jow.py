# #Verifique se um número é múltiplo de 3 ou 5, mas não de 7.
num = int(input("Digite um número: "))

if (num % 3 == 0 or num % 5 == 0) and num % 7 != 0:
    print("O número digitado é múltiplo de 3 ou 5, mas não é múltiplo de 7")
elif (num % 3 == 0 or num % 5 == 0) and num % 7 == 0:
    print("O número digitado é múltiplo de 3 ou 5 e também de 7")
else:
    print("O número não é múltiplo de 3 nem de 5")
