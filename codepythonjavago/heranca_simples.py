class Animal:
    def __init__(self, especie, nome):
        self: especie = especie
        self: nome = nome

    def emitirsom(self):
        pass


class Cachorro(Animal):
    def emitirsom(self):
        return "AU AU"


class Gato(Animal):
    def emitirsom(self):
        return "MIAU"
