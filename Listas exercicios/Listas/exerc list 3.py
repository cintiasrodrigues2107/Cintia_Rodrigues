#[LIST] Atualizar elemento com uma operação
#Tarefa: Crie uma lista com três inteiros. Atualize o último elemento para a soma dos dois primeiros. Exiba a lista.
#Use: int(), input(), indexação lista[i], print()
#Tipos: int, list.
#Conceitos: operadores aritméticos (+), acesso/atribuição por índice.

num1 = int(input("Digite primeiro numero da lista:"))
num2 = int(input("Digite primeiro numero da lista:"))
num3 = int(input("Digite primeiro numero da lista:"))

lista = [num1, num2, num3]

print("Primeira número da lista:", lista[0])

lista_nova = lista[0] + lista[1]
print("soma dos dois primeiros numeros:" ,lista_nova)

lista[2] = lista_nova
print("Lista após inclusão do novo último elemento:", lista)