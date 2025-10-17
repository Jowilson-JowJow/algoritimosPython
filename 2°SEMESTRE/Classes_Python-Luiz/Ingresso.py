class Ingresso:
    def __init__(self, preco, setor):
        self.preco = preco
        self.setor = setor

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco
        print(f"Novo preço do ingresso: R${self.preco}")

    def mostrar_setor(self):
        print(f"Setor do ingresso: {self.setor}")

class IngressoVIP(Ingresso):
    def __init__(self, preco, setor, camarote, open_bar, open_food, estacionamento):
        super().__init__(preco, setor)
        self.camarote = camarote
        self.open_bar = open_bar
        self.open_food = open_food
        self.estacionamento = estacionamento

    def pegar_bebida(self):
        if self.open_bar:
            print("Pegando bebida no open bar!")
        else:
            print("Sem open bar disponível.")

    def acessar_camarote(self):
        if self.camarote:
            print("Acessando o camarote VIP!")
        else:
            print("Camarote VIP não disponível.")

ingresso_normal = Ingresso(100, "Setor A")
ingresso_normal.mostrar_setor()
ingresso_normal.alterar_preco(120)

ingresso_vip = IngressoVIP(300, "Setor VIP", True, True, True, True)
ingresso_vip.mostrar_setor()
ingresso_vip.pegar_bebida()
ingresso_vip.acessar_camarote()

ingresso_vip2 = IngressoVIP(250, "Setor B", False, False, True, True)
ingresso_vip2.mostrar_setor()
ingresso_vip2.pegar_bebida()  # Sem open bar
ingresso_vip2.acessar_camarote()  # Sem camarote

