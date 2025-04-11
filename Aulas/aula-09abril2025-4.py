#faça um algaritmo para pedir o salario faça o reajuste conforme a a tabela dado
salario=float(input('Digite o seu salario atual: '))
if(salario>1000):
    print('Seu salario foi reajustado em 5%%. O novo salario é %.2f'%(salario*1.05))
elif(salario>=500 and salario<=1000):
    print('Seu salario foi reajustado em 10%%.\nO novo salario é %.2f'%(salario*1.10))
else:
    print('Seu salario foi reajustado em 15%%\nO novo salario é %.2f'%(salario*1.15))
