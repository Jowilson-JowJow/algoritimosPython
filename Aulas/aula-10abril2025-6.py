#exercicio 11 da segunda foto
salario=float(input('Digite o salario do colaborador: '))
if salario>1501.34:
    aumento=salario*0.0519
    salario1=salario+aumento
    print(salario)
    print('O salario foi aumentado em 5,19%')
    print('%.2f'%aumento)
    print('%.2f'%salario1)
elif salario>=709.73 and salario<=1501.33:
    aumento=salario*0.1097
    salario1=salario+aumento
    print(salario)
    print('O salario foi aumentado em 10,97%')
    print('%.2f'%aumento)
    print('%.2f'%salario1)
elif salario>=280.56 and salario<=709.72:
    aumento=salario*0.1539
    salario1=salario+aumento
    print(salario)
    print('O salario foi aumentado em 15,39%')
    print('%.2f'%aumento)
    print('%.2f'%salario1)
# elif salario<=280.55:
#     aumento=salario*0.2251
#     salario1=salario+aumento
#     print(salario)
#     print('O salario foi aumentado em 22,51%')
#     print('%.2f'%aumento)
#     print('%.2f'%salario1)
else:
    aumento=salario*0.2251
    salario1=salario+aumento
    print(salario)
    print('O salario foi aumentado em 22,51%')
    print('%.2f'%aumento)
    print('%.2f'%salario1)