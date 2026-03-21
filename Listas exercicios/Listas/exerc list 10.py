'''
[DICT  - desafio] Agenda (CRUD simples) com ordenação de nomes

Tarefa: Comece com agenda = {"Ana": "1111-1111", "Bruno": "2222-2222"}. 
Adicionar um novo contato (nome→telefone)
Atualizar o telefone de um contato informado (se existir)
Remover um contato pelo nome (se existir)
Exibir a lista ordenada de nomes de contatos
Tipos: str, dict, list (para a lista ordenada, se desejar armazenar).Conceitos: CRUD em dicionários, teste de existência, ordenação de chaves.Use: input(), acesso/atribuição agenda[nome] = tel, in, pop(), sorted(agenda.keys()), print()

Algoritimo:
1. Criar o dicionario agenda
2. Adição de um novo contato nome:telefone
3. Se o contato informado existir, atualizar o telefone
4. Remover um contato pelo nome
5. Exibe a lista ordenada de nomes de contato

'''

agenda = {"Ana": "1111-1111", "Bruno": "2222-2222"}
print(agenda)

novo_nome = input("Digite o nome do novo contato: ")
novo_telefone = input("Digite o telefone do novo contato: ")
agenda[novo_nome] = novo_telefone
print(agenda)

nome_atualizar = input("Digite o nome do contato que deseja atualizar: ")
telefone_novo = input("Digite o novo telefone: ")

(nome_atualizar in agenda) and agenda.__setitem__(nome_atualizar, telefone_novo)
print("Após atualizar contato: ", agenda)

nome_remover = input("Digite o nome do contato que deseja remover: "))
agenda.pop(nome_remover)
print(agenda)

nomes_ordenados = sorted(agenda.keys())
print("Nomes ordenados: ", nomes_ordenados)

