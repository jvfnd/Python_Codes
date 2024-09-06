class Animal:
    def __init__(self, nome):
        self.nome = nome
    def emitirsom(self):
        pass

class Mamifero(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def amamentar(self):
        print(f"{self.nome} está amamentando.")

class Ave(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    def voar(self):
        print(f"{self.nome} está voando")

class Morcego(Mamifero, Ave):
    def __init__(self, nome):
        super().__init__(nome)
    def emitirsom(self):
        print("Morcego fazendo ruídos noturnos.")

morcego = Morcego("Batemane")
morcego.emitirsom()
morcego.amamentar()
morcego.voar()