#[LIST] Remova um número se ele existir:
#Tarefa: Leia quatro inteiros e crie uma lista. Leia um valor alvo e remova se ele estiver na lista. Mostre o tamanho antes e depois.
#Use: int(), input(), in, remove(), len(), print()
#Tipos: int, list.
# Conceitos: teste de pertencimento, tratamento simples de remoção, função len().

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))
num4 = int(input("Digite um número: "))

numeros = [num1, num2, num3, num4]
print("Primeira Lista:", numeros)

print("Tamanho da lista 'numeros':", len(numeros))

alvo = int(input("Digite o número que deseja remover:" ))
print("Valor removido",alvo)

if alvo in numeros:
    numeros.remove(alvo)
    print("Tamanho da lista 'numeros':", len(numeros))
    print("Lista nova depois da remoção:", numeros)
else: 
    print("Não consta na lista")




