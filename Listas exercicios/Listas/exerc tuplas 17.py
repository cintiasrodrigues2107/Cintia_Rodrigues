'''
TUPLE - desafio] Organizar valores sem mexer na tupla original

Tarefa: Leia quatro números em uma tupla e exiba: 
a tupla original
uma lista ordenada apenas para visualização
o tipo da variável ordenada
Objetivo: mostrar diferença entre tupla e lista sem precisar modificar nada.Use: sorted(), print(), type()

Algoritimo:
1. Leia quatro números em uma tupla
2. Exibir a tupla original
3. Exibir a lista ordenada
4. O tipo de variável ordenada

'''
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o primeiro número: "))
n3 = int(input("Digite o primeiro número: "))
n4 = int(input("Digite o primeiro número: "))

tupla_original = (n1, n2, n3, n4)
print(tupla_original)

lista_ordenada = sorted(tupla_original)
print(lista_ordenada)

print("Tipo da variavel ordenada: ", type(lista_ordenada))
