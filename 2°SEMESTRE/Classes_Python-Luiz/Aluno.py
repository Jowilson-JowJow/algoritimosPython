class Aluno:
    def __init__(self, nome, ra, nota1, nota2, nota3, nota4):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def calcular_media(self):
        """Calcula a média das notas do aluno"""
        return (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4

    def mostrar_situacao(self):
        """Determina a situação do aluno com base na média"""
        media = self.calcular_media()
        if media >= 7:
            situacao = "APROVADO"
        elif media >= 5:
            situacao = "EXAME"
        else:
            situacao = "REPROVADO"
        
        return f"Aluno: {self.nome}\nRA: {self.ra}\nMédia: {media:.2f}\nSituação: {situacao}"

aluno1 = Aluno("Maria Silva", "123456", 7.5, 8.0, 6.0, 9.0)
aluno2 = Aluno("João Oliveira", "654321", 4.0, 5.0, 6.0, 3.0)

print(aluno1.mostrar_situacao())
print("\n" + "="*30 + "\n")
print(aluno2.mostrar_situacao())