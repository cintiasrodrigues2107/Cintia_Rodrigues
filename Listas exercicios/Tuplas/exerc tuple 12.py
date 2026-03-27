'''
[TUPLE] Acessar elementos da tupla

Tarefa: Leia três frutas e coloque em uma tupla. Depois leia uma fruta e diga se ela está ou não na tupla.
 Orientações: 
 
usar in
 
usar input()
 
tipo: str, tuple
 
conceito: operador de pertinência

Algoritmo:
1. Crie uma tupla com três frutas;
2. Exiba a tupla;
3. Leia a fruta e diga se ela está ou não na tupla;

'''
nome1 = input("Digite primeiro nome: ")
nome2 = input("Digite segundo nome: ")

usuario = (nome1, nome2)
print(usuario)

print(type(usuario))

