def red_min(anos_fumados, cigarros_por_dia):
    resul = anos_fumados * 365 * cigarros_por_dia * 10
    return resul


def red_dias(reducao_em_minutos):
    resul = reducao_em_minutos / (24 * 60)
    return resul



def cigarettesperday():
    cigarros = int(input("Quantidade de cigarros por dia:"))
    return cigarros



def yearssmoking():
    anosfumando = float(input("Quantidade de anos fumando:"))
    return anosfumando
