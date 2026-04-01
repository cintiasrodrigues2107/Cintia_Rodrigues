'''
Listas de exercícios - Estruturas de Controle

1. Solicite ao usuário que informe um número e depois exiba se o número é positivo, negativo ou zero.
'''


num = float(input("Digite um número: "))

if num < 0:
    print("O número é negativo.")
elif num > 0:
    print("O número é positivo.")
else:
    print("O número é zero.")


