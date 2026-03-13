# Leia metros (int). Converta para km inteiros com //= 1000 e guarde metros restantes com %= (em outra variável).

metros = int(input("Quantos metros: "))
converta = metros
converta //= 1000
print(converta)

restante = metros
restante %= 1000
print(restante)
