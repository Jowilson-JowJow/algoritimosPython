class Filme:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def play(self):
        print(f"Dando play no filme: {self.nome}")

class Acao(Filme):
    def explodir(self):
        print("Explosão na tela!")

class Drama(Filme):
    def chorar(self):
        print("Cena emocionante... lágrimas caem.")

class Suspense(Filme):
    def plot_twist(self):
        print("Reviravolta surpreendente!")

filme1 = Acao("Missão Impossível", 120)
filme2 = Drama("À Procura da Felicidade", 110)
filme3 = Suspense("Garota Exemplar", 130)

filme1.play()
filme1.explodir()

filme2.play()
filme2.chorar()

filme3.play()
filme3.plot_twist()