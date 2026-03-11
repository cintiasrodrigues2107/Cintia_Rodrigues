# Leia estoque (int). Subtraia venda com -=, depois reposição com +=, por fim %= 6.

estoque = int(input("Qual o valor do estoque: "))
estoque -= int(input("Qual novo valor após a venda: "))
estoque += int(input("Qual novo valor após reposição: "))
estoque %= 6

print("Qual valor do novo estoque: ", estoque)