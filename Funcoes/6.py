#Crie uma função que receba uma lista de números e retorne a média dos valores.

def media(lista):
    if not lista:  # Verifica se a lista está vazia
        return None  # Retorna None se a lista estiver vazia
    
    soma = sum(lista)  # Calcula a soma dos números na lista
    quantidade = len(lista)  # Obtém a quantidade de números na lista
    
    media = soma / quantidade  # Calcula a média
    return media

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))
lista = [num1, num2, num3]

resultado = media(lista)
if resultado is not None:
    print(f"A média dos números é: {resultado}")
else:
    print("A lista está vazia. Não é possível calcular a média.")
    