def somadeposicaodovetor(vetor, x, y):
    soma = vetor[x] + vetor[y]
    return soma


def criarvetorint(tamanho):
    vetor = [0] * tamanho
    for i in range(tamanho):
        vetor[i] = int(input("Digite o valor da posição {}: ".format(i)))
    return vetor


def maiorvalordovetor(vetor):
    maior = vetor[0]
    for i in range(1, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
    return maior

def menorvalordovetor(vetor):
    menor = vetor[0]
    for i in range(1, len(vetor)):
        if vetor[i] < menor:
            menor = vetor[i]
    return menor