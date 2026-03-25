'''
#[DICT - CONTINUIDADE DO EXERCÍCIO ANTERIOR] 
Adicionar uma nova chave nota
Tarefa: Partindo de um aluno com nome e idade, leia uma nota (float) e adicione a chave "nota". Exiba o dicionário.
 Use: float(), input(), atribuição dict["nota"] = valor, print()
 Tipos: float, dict.
 Conceitos: atualização/adição de chave, tipos numéricos.

 Algoritmo:
 1. Continuar o dicionario anterior {aluno}
 2. Acrescentar uma chave nova (nota);
 3. Nota (float) com a chave "nota"
 4. Exiba o dicionário
 
'''
aluno = {}
print(aluno)

nome = input("Digite um nome: ")
idade = int(input("Digite sua idade: "))

aluno = {"nome": nome, "idade": idade}

nota = float(input("Digite uma nota: "))

aluno["nota"] = nota

print(aluno)

