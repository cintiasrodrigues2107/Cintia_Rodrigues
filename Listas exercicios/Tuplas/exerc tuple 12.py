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

# Lendo três frutas e colocando em uma tupla
fruta1 = input("Digite a primeira fruta: ")
fruta2 = input("Digite a segunda fruta: ")
fruta3 = input("Digite a terceira fruta: ")

tupla_frutas = (fruta1, fruta2, fruta3)
print(tupla_frutas)

# Lendo uma fruta para verificar
busca = input("Digite uma fruta para verificar: ")

# Verificando se está na tupla
if busca in tupla_frutas:
    print("A fruta está na tupla!")
else:
    print("A fruta NÃO está na tupla!")

