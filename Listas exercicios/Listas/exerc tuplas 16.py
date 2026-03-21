'''
[TUPLE - desafio] Tupla de notas com média (sem alterar a tupla)

Tarefa: Leia três notas (float) e armazene em uma tupla. Exiba a tupla e a média das notas.
 Use: float(), sum(), len(), print()
 Sem alterar tupla.
Algaritimo:
Ler 3 notas em float
Armazenar as 3 notas em tuplas
Calcular a média das notas
Exibir a tupla e a média das notas
'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

notas = (nota1, nota2, nota3)
print("Tuplas de notas: ", notas)

media = sum(notas) / len(notas)
print("Média das notas", media)
