#[LIST - desafio] Fila: chegadas, prioridade e atendimento
# Tarefa: Inicie fila = ["Ana", "Bruno"]. Leia dois nomes e adicione (use extend). Leia um cliente prioritário e insira na posição 1. Atenda (remova e capture) o primeiro com pop(0). Exiba a fila a cada etapa.
# Use: input(), extend(), insert(), pop(), print()
# Tipos: str, list.
# Conceitos: estrutura de fila, operações de inserção/remoção, ordem.
'''
Algoritimo:
1. Iniciar uma fila = 
2. Ler dois nomes
3. Adicionar eles a lista utilizando extend ()
4. Ler um cliente que seja prioritario
5. O cliente prioritario deve ser inserido na posição 1(indice 1).
6. Atender o cliente
    Remover com pop()
7. Exibição da fila atualizada
'''



fila = ["Ana", "Bruno"]
print("Fila inicial", fila)

nome3 = input("Digite um nome:")
nome4 = input("Digite um nome:")
fila.extend([nome3, nome4])
print("Após adicionar dois nomes: ",fila)

prioritario = input("Digite o nome do cliente prioritário: ")
fila.insert(0, prioritario)
print("Após inserir o cliente prioritario na posição 0: ", fila)

atendido = fila.pop(0)
print("Cliente atendido: ",atendido)
print("Fila final: ", fila)