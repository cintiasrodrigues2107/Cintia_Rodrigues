'''
# [DICT - desafio] Atualizar preço e quantidade; calcular o total 

Tarefa: Leia produto = {"nome": str, "preco": float, "quantidade": int}. Aplique aumento percentual ao preço e some 2 unidades na quantidade. Calcule total = preco * quantidade e exiba.
 Use: float(), int(), input(), acesso/atribuição por chave, print()
 Tipos: str, float, int, dict.
 Conceitos: operadores aritméticos (*, +), atualização de valores no dict.

Algoritmo:
1. Leia um produto = {"nome": str, "preco": float, "quantidade": int}
2. exiba dicionario antes;
3. Aplique um percentual ao preço
4. Exiba após o percentual
5. Some 2 unidades na quantidade;
6. exiba depois da soma
4. Calcule total = preço * quantidade
5. Exiba o total
'''

produto = {}
nome = input("Digite um nome: ")
preco = float(input("Digite um preço: "))
quantidade = int(input("Digite a quantidade: "))

produto = {"nome": nome, "preco": preco, "quantidade": quantidade}
print("Dicionario inicial", produto)

aumento = float(input("Digite o aumento: "))
print(aumento)

produto["preco"] += float((produto["preco"] * aumento) / 100)
print("Dicionario após aumento", produto)

produto["quantidade"] += 2
print("Dicionario após soma", produto)

total = produto["preco"] * produto["quantidade"]
print("Total da conta:", produto)

print(f"{total:.2f}")

