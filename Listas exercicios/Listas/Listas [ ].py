frutas = ["maçã", "banana", "uva"]
numeros = [1, 2, 3, 4]

# Acessando elementos:
print("Primeira fruta:", frutas[0])     #"maçã"
print("Última fruta:", frutas[-2])      #"banana"

# Alterando elementos:
frutas[1] = "banana_prata"
print("Após alterar:", frutas)

# Adicionando elementos:
frutas.append("morango")           # adiciona no final na lista
frutas.insert(1, "pera")           # adiciona na posição 1
print("Após adicionar:", frutas)

# Removendo elementos:
frutas.remove("uva")                #remove pelo valor
ultima = frutas.pop()               # remove e mostra o último da lista
print("Após remover 'uva' e pop():", frutas, "| última removida:", ultima)

# Tamanho (quantidade de elementos):
print("Tamanho da lista 'frutas':", len(frutas))
print("Tamanho da lista 'numeros':", len(numeros))

#Fatiamento (slicing):
print("Fatiamento [0:2]:", frutas[0:2])

# Verificar se um item está na lista:
print("Tem 'maçã'?", "maçã" in frutas)

#Outros operadores úteis
print("Lista original 'numeros':", numeros)
print("Soma dos números:", sum(numeros))
print("Maior número:", max(numeros))
print("Menor número:", min(numeros))

numeros.reverse()
print("Reversa:" , numeros)
numeros.sort()
print("Ordenada crescente:", numeros)
numeros.sort(reverse=true)
print("Ordenada decrescente:", numeros)

# Iterar sobre lista
for fruta in frutas:
    print("Frutas:", fruta)

# List comprehension (exemplo simples)
quadrados = [n * n for n in [1, 2, 3, 4, 5,]]
print("Quadrados:", quadrados)