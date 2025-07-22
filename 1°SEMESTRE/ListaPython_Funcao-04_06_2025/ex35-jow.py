#Crie uma função que receba uma data (dia, mês, ano) e diga se ela é válida (considere apenas datas do calendário gregoriano, sem considerar anos bissextos).
def data_valida(dia, mes, ano):
    if mes < 1 or mes > 12:
        return False
    if dia < 1:
        return False

  
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if dia > dias_por_mes[mes - 1]:
        return False

    return True


dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

if data_valida(dia, mes, ano):
    print('A data é válida!')
else:
    print('Data inválida.')
