# Leia base (float). Aplique *= 1.05 (aumento 5%), depois -= 2 (taxa), depois /= 2.

base = float(input("Qual valor: "))
base *= 1.05
print("Valor com aumento de 5%: " , base)

base -= 2
print("Valor com a taxa 2%: " , base)

base /= 2
print("Valor dividido por 2: " , base)
