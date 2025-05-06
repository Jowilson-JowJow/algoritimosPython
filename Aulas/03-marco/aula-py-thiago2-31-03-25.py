#um if dentro do if
nome=input("Digite o nome do aluno:")
nota=int(input("digite a nota do aluno:"))

if nota>=6:
    if nota>=6 and nota<8:
        print("conceito B")
    else:
        print("conceito A")
else:
    print("conceito C")