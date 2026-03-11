# Leia um contador (int) e um passo (int). Faça contador += passo duas vezes. Mostre o resultado.

contador = int(input("Digite valor contador: "))
passo = int(input("Digite valor passo: "))

contador += passo
print("passo 1: ", contador)

contador += passo
print("passo 2: ", contador)
