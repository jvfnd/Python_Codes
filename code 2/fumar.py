from funcaofumo import *


cigarros_por_dia = cigarettesperday()
anos_fumados = yearssmoking()

a = red_min(anos_fumados, cigarros_por_dia)
b = red_dias(a)
print(f"Redução do tempo de vida {b} dias")