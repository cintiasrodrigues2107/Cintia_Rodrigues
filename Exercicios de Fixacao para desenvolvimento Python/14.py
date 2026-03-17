#Leia uma quantidade de minutos (int) e converta para horas e minutos (ex.: 130 -> 2h10)

minutos = int(input("Digite a quantidade em m: "))

horas = minutos // 60
resto = minutos % 60

print(f"{horas}h{resto: 02d}min")