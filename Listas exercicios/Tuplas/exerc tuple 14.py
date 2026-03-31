'''
[TUPLE] Exibir maior e menor valor
Tarefa: Leia quatro números inteiros, coloque em uma tupla e exiba o maior e o menor.
 Orientações: 
 
funções: max(), min()
 
tipos: int, tuple
 
conceito: operações básicas de agregação

Algoritmo:
1.Ler o primeiro número inteiro;
2.Ler o segundo número inteiro
3.Ler o terceiro número inteiro
4.Ler o quarto número inteiro
5.Criar uma tupla com os quatro números
6.Calcular o maior valor usando max()
7.Calcular o menor valor usando min()
8.Exibir o maior valor
9.Exibir o menor valor

'''

# Lendo quatro números inteiros e criando a tupla
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))

tupla_numeros = (n1, n2, n3, n4)
print(tupla_numeros)


# Encontrando o maior e o menor valor
maior = max(tupla_numeros)
menor = min(tupla_numeros)

print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")