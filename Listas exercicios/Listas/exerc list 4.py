#[LIST - desafio] Notas: subtituir a menor nota, ordenar e recalcular a média
# Tarefa: Leia três notas (float) em uma lista. Calcule a média. Substitua a menor nota por uma nova informada. Ordene a lista e mostre a nova média.
# Use: float(), input(), min(), list.index(), atribuição por índice, sort(), sum(), len(), print()
# Tipos: float, list.
# Conceitos: mutabilidade, ordenação in-place, média aritmética.

n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
n3 = float(input("Digite a terceira nota:"))
notas = [n1, n2, n3]
print("Lista de notas:", notas)

media = sum(notas[:3]) / 3
print("Valor da média:", media)

nova_nota = float(input("Digite a nova nota: "))
print("Nova nota:", nova_nota)

if n1 < n2 and n1 < n3:
    notas[0] = nova_nota
    print("# 1")
elif n2 < n1 and n2 < n3:
    notas[1] = nova_nota
    print("# 2")
elif n3 < n1 and n3 < n2:
    notas[2] = nova_nota
    print("# 3")

media = sum(notas[:3]) / 3
print("Valor da média:", media)
notas.sort()
print("Lista notas nova:", notas)








#notas[1] = "banana_prata"
#print("Após alterar:", frutas)