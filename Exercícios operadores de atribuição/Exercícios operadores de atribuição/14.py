# Leia dias (int). Mantenha apenas os dias restantes após converter para semanas (7 dias) usando %=.

dias = int(input("Quantos dias: "))
dias %= 7 

print("Quantos dias restaram após virgula: ",dias)