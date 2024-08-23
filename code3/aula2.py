from funcao import criarvetorint, somadeposicaodovetor

lista = criarvetorint(8)

x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

soma = somadeposicaodovetor(lista, x, y)

print("A soma dos valores nas posições x e y é {}.".format(soma))


