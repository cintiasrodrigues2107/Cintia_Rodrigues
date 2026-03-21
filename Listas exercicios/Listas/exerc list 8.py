''''
[DICT] Remover uma chave com segurança

Tarefa: Leia produto = {"nome": str, "preco": float}. Tente remover a chave "desconto" se existir, sem gerar erro. Mostre antes e depois.
 Use: input(), float(), dict.pop("chave", valor_padrao), print()
 Tipos: str, float, dict.
 Conceitos: remoção segura, estado antes/depois.

 1. Ler um produto com nome e preço
 2. Tentar remover a chave desconto se ela existir e não deve gerar erro
 3. Exibir antes e depois de cada alteração
''''
#todo dicionario possui uma dupla de chave:valor

produto = {}
print(produto)

nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))

produto = {"nome": nome, "preco": preco}
print("Antes da remoção: ", produto)

#Tentar remover a chave 'desconto' sem gerar erro caso ela não exista
produto.pop("desconto", None)

print("Depois da remoção: ", produto)

