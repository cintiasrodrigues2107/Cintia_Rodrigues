#Crie uma função que receba uma lista de números e retorne o maior número da lista.

def maior_numero(lista):
    return max(lista)  # Utiliza a função max para encontrar o maior número na lista


num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))
lista = [num1, num2, num3]

maior = maior_numero(lista)
print(f"O maior número é: {maior}")