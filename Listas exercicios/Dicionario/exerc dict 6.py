#[DICT] Criar e exibir dicionário de aluno
'''
Tarefa: Leia nome e idade. Crie aluno = {"nome": ..., "idade": ...} e exiba o dicionário e seu tipo.
 Use: input(), int(), literal {}, acesso por chave dict["chave"], print(), type()
 Tipos: str, int, dict.
 Conceitos: mapeamento chave-valor, criação e exibição.

 Algoritimo:
1. Leia nome e idade 
2. crie um dicionario alunos com estes nomes e idades
3. exiba o dicionario e seu tipo
4. Use: input(), int(), literal {}, acesso por chave dict["chave"], print(), type()
5. Tipos: str, int, dict.
 
'''
aluno = {}
print(aluno)

nome = input("Digite um nome: ")
idade = int(input("Digite sua idade: "))

aluno = {"nome": nome, "idade": idade,}

print(f" {aluno}, {type(aluno)}")
