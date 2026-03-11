# Crie um programa que solicita ao usuário os dados do aluno (nome, idade, altura, contato) 
# e depois exiba a informação na tela.

nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
altura = float(input("Digite a altura do aluno: "))
contato = input("O contato do aluno é: ")
aprovado = bool(input("O aluno foi aprovado? (True/False): "))

print("Nome: ", nome)
print("Idade: ", idade)
print("Altura: ", altura, "m" )
print("Contato: ", contato)
print("Aprovado: ", aprovado)