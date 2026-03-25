# Dicionarios armazenam pares chave:valor

# criando dicionarios:
aluna = {"id": 1, "nome": "Caroline", "nota": 9.2}
pessoa = {"nome": "Ana", "idade": 25}

# Acessar valores por chave:
print("Nome da pessoa:", pessoa ["nome"])

# Adicionar e alterar chaves/valores:
pessoa["cidade"] = "Florianopolis"  # adiciona nova chave
pessoa["idade"] = 26                # altera valor existente
print("pessoa atualizada:", pessoa)

# Remover chave:
removido = pessoa.pop("idade")
print("Valor removido (idade):", removido)
print("Após pop('idade'):", pessoa)

#Tamanho:
print("Quantidade de chaves em 'aluna':", len(aluna))

# Lista chaves, valores e itens (pares):
print("Chaves de 'aluna':", list(aluna.keys()))
print("Valores de 'aluna':", list(aluna.values()))
print("Itens de 'aluna':", list(aluna.items()))


# Verificar se uma chave existe:
print("Chave 'nota' existe?", "nota" in aluna)

# Obter valor com padrão (evita erro se chave não existir)
print("turma (com default):", aluna.get("turma", "não cadastrada"))

# Atualizar várias chaves de uma vez:
aluna.update({"nota": 9.5, "turma": "A"})
print("Aluna após update:", aluna)

# Iterar sobre dict
for chave, valor in aluna.items()
    print(f"{chave} -> {valor}")