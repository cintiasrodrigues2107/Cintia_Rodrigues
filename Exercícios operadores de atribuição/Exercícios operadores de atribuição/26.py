# Leia dois inteiros a e b. Em a: a += b, a *= 2, a %= 7.
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

A += B
print("Resultado de A + B é: " , A)

A *= 2
print("Resultado de A * 2 é: " , A)

A %= 7
print("Resultado de A mod 7 é: " , A)