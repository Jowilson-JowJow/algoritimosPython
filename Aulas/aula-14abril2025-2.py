valorHora=float(input('Digite o valor da hora de trabalho do colaborador: '))
quantHora=float(input('Digite quantas horas de trabalho/mês do colaborador: '))
salarioBruto=valorHora*quantHora
if (salarioBruto<=900):
    fgts=salarioBruto*0.11
    inss=salarioBruto*0.10
    ir=salarioBruto*0.05
    totalDesc=inss
    salarioLiquido=salarioBruto-totalDesc
    print('Salario Bruto: ',((valorHora,'*',quantHora,)),'        :R$  %.2f'%salarioBruto)
    print('(-) IR (5%%)                                :R$  %.2f'%ir)
    print('(-) INSS (10%%)                             :R$  %.2f'%inss)
    print('FGTS (11%%)                                 :R$  %.2f'%fgts)
    print('total de descontos                         :R$  %.2f'%totalDesc)
    print('Salário Liquido                            :R$  %.2f'%salarioLiquido)
elif (salarioBruto<=1500):
    fgts=salarioBruto*0.11
    inss=salarioBruto*0.10
    ir=salarioBruto*0.05
    totalDesc=inss+ir
    salarioLiquido=salarioBruto-totalDesc
    print('Salario Bruto: ',((valorHora,'*',quantHora,)),'        :R$  %.2f'%salarioBruto)
    print('(-) IR (5%%)                                :R$  %.2f'%ir)
    print('(-) INSS (10%%)                             :R$  %.2f'%inss)
    print('FGTS (11%%)                                 :R$  %.2f'%fgts)
    print('total de descontos                         :R$  %.2f'%totalDesc)
    print('Salário Liquido                            :R$  %.2f'%salarioLiquido)
elif (salarioBruto<=2500):
    fgts=salarioBruto*0.11
    inss=salarioBruto*0.10
    ir=salarioBruto*0.1
    totalDesc=inss+ir
    salarioLiquido=salarioBruto-totalDesc
    print('Salario Bruto: ',((valorHora,'*',quantHora,)),'        :R$  %.2f'%salarioBruto)
    print('(-) IR (5%%)                                :R$  %.2f'%ir)
    print('(-) INSS (10%%)                             :R$  %.2f'%inss)
    print('FGTS (11%%)                                 :R$  %.2f'%fgts)
    print('total de descontos                         :R$  %.2f'%totalDesc)
    print('Salário Liquido                            :R$  %.2f'%salarioLiquido)
elif (salarioBruto>2500):
    fgts=salarioBruto*0.11
    inss=salarioBruto*0.20
    ir=salarioBruto*0.1
    totalDesc=inss+ir
    salarioLiquido=salarioBruto-totalDesc
    print('Salario Bruto: ',((valorHora,'*',quantHora,)),'        :R$  %.2f'%salarioBruto)
    print('(-) IR (5%%)                                :R$  %.2f'%ir)
    print('(-) INSS (10%%)                             :R$  %.2f'%inss)
    print('FGTS (11%%)                                 :R$  %.2f'%fgts)
    print('total de descontos                         :R$  %.2f'%totalDesc)
    print('Salário Liquido                            :R$  %.2f'%salarioLiquido)
