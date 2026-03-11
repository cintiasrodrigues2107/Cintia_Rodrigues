# Leia um número (int), aplique n %= 2 e imprima.
# 0 = par, 1 = ímpar

n = int(input("Qual o número: "))
n %= 2

if n==0:
    print("O número é par: ")
else:
    print("O número é ímpar: ")