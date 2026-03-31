'''
[TUPLE] Contar quantas vezes um número aparece

Tarefa: Leia quatro números inteiros e crie uma tupla. Depois leia um número e diga quantas vezes ele aparece na tupla.
 Orientações: 
 
método: tuple.count()
 
tipos: int, tuple

Algoritmo:
1. Crie uma tupla com quatro números inteiros;
2. Exiba a tupla;
3. Exiba quantas vezes este número aparece;

'''
# Lendo quatro números inteiros e criando a tupla
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))

tupla_numeros = (n1, n2, n3, n4)
print(tupla_numeros)

# Lendo o número a ser contado
busca = int(input("Digite um número para contar: "))

# Contando quantas vezes aparece
quantidade = tupla_numeros.count(busca)

print(f"O número {busca} aparece {quantidade} vez(es) na tupla.")
