'''
[TUPLE] Criar e exibir uma tupla simples

Tarefa: Leia dois nomes do usuário e coloque-os em uma tupla. Depois exiba a tupla e o tipo dela.
 Orientações: 
 
usar input(), print(), type()
 
usar tupla no formato (valor1, valor2)
 
tipo trabalhado: str, tuple

Algoritmo:
1. Crie uma tupla com dois nomes de usuarios;
2. Exiba a tupla;
3. Exiba o tipo dela

'''
nome1 = input("Digite primeiro nome: ")
nome2 = input("Digite segundo nome: ")

usuario = (nome1, nome2)
print(usuario)

print(type(usuario))

