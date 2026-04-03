#Crie uma função que receba uma palavra e verifique se ela é um palíndromo
#(lê igual de trás para frente).

def palindromo(palavra):
       
    # Inverte a palavra
    palavra_invertida = palavra[::-1]
    
    # Compara a palavra original com a invertida
    return palavra == palavra_invertida

# Exemplo de uso
palavra = input("Digite uma palavra: ")
if palindromo(palavra):
    print(f"'{palavra}' é um palíndromo.")
else:
    print(f"'{palavra}' não é um palíndromo.")