#Crie uma função que receba uma string e retorne a quantidade de caracteres que ela possui.

def contar_caracteres(qualquer_coisa):
    return len(qualquer_coisa) 

frase = input("Digite uma frase: ")
quantidade = contar_caracteres(frase)
print(f"A frase '{frase}' possui {quantidade} caracteres.")