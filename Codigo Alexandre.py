print("SENAC")
nome = input("Digite se nome: ")
idade = int(input("Digite a sua idade: "))
contato = input("Informe o seu contato: ")

p1 = input("Você já programou? (S/N)")
p2 = int(input("Você gosta mais de lógica ou design (1/2)"))
p3 = input("Você tem interesse em design? (S/N)")

if p1 == "S" and p2 == 2 and p3 == "N":
    print("Seu curso é Desenvolvimento Web")
elif p1 == "N" and p2 == 2 and p3 == "S":
    print("Seu curso é Ux/design")
elif p1 == "S" and p2 == 1 and p3 == "N":
    print ("Seu curso é Desenvolvimento de software")
else:
    print("Não tem curso")