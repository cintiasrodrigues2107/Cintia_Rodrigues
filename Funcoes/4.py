#Crie uma função que receba uma lista de números e retorne o maior número da lista.

def maior_numero(lista):
    if not lista:  # Verifica se a lista está vazia
        return None  # Retorna None se a lista estiver vazia
    
    maior = lista[0]  # Inicializa o maior número com o primeiro elemento da lista
    
    for numero in lista:
        if numero > maior:
            maior = numero
            
    return maior


num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))
lista = [num1, num2, num3]

maior = maior_numero(lista)
print(f"O maior número é: {maior}")