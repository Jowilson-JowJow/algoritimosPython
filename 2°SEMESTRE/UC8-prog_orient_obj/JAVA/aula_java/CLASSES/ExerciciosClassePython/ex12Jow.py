# 12 - Classe Filme: Crie uma super classe que modele um Filme. Esta classe deve possuir os seguintes atributos:
# Nome;
# Duração;
# Método:
# Play(): deve exibir que foi dado play no filme;
# Subclasses:
# Defina as subclasses de Filme, exemplo Ação, Drama e Suspense. Após a criação das subclasses você deve criar novos métodos específicos a cada subclasse, ex: explodir() em Ação.

class Filme:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def play(self):
        return "Iniciando o Filme!!!"

class Acao(Filme):
    def explodir(self):
        print(f"O filme {self.nome} teve uma grande explosão!!!")

class Drama(Filme):
    def chorar(self):
        print(f"O filme {self.nome} emocionou o público às lágrimas!")

class Suspense(Filme):
    def assustar(self):
        print(f"O filme {self.nome} deixou todos tensos e assustados!")



filme1 = Acao("Missão Impossível", "2h30min")
filme2 = Drama("À Procura da Felicidade", "2h05min")
filme3 = Suspense("O Sexto Sentido", "1h50min")


filme1.play()
filme1.explodir()

filme2.play()
filme2.chorar()

filme3.play()
filme3.assustar()
