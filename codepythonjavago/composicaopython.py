class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

    def ligar(self):
        print("O Motor está ligado")

    def desligar(self):
        print("O motor está desligado")


class Pneu:
    def __init__(self, marca, tamanho):
        self.marca = marca
        self.tamanho = tamanho

    def inflar(self):
        print("O pneu está inflado")

    def desinflar(self):
        print("O pneu está desinflado")


class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor("Gasolina", 150)
        self.pneus = [Pneu("Michellin", 19)for _ in range(4)]

    def ligar(self):
        self.motor.ligar()
        print("O carro está ligado")

    def desligar(self):
        self.motor.desligar()
        print("O carro foi desligado")

    def trocar_pneu(self, indice, novo_pneu):
        self.pneus[indice] = novo_pneu
        print(f"Pneu {indice + 1} trocado.")


carro = Carro("Corolla", "kdoaksd")
carro.ligar()

novo_pneu = Pneu("Firelli", 17)
carro.trocar_pneu(2, novo_pneu)
carro.desligar()
