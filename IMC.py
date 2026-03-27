'''
#Código para executar o cálculo do IMC e dar o resultado em tela:
'''
nome = input("Digite o nome: ")
peso = float(input("Informe o peso em Kg: "))
altura = float(input("Informe a altura em metros (ex. 1.75): "))

imc = peso / (altura ** 2)
print(f"{nome} , O seu IMC é: {imc: .2f}")

baixo_peso = imc < 18.5
peso_normal = 18.5 <= imc < 25
sobrepeso = 25 <= imc < 30
obesidade = imc >= 30

print(baixo_peso)
print(peso_normal)
print(sobrepeso)
print(obesidade)

'''
#Código para executar o cálculo do IMC e dar o resultado em tela:
Algoritimo:
1. Iniciar o algoritmo;
2. Solicitar o peso (kg) e ler o valor;
3. Solicitar a altura(m) e ler o valor;
4. Calcular o IMC = peso / (altura * altura)
5. SE o IMC for menor que 18.5;
    Exibir: "IMC = X.XX - Magreza"
6. SE o IMC for maior ou igual a 18.5 e menor que 25;
    Exibir: "IMC = X.XX - Normal"
7. SE o IMC form maior ou igual a 25 e menor que 30:
    Exibir: "IMC = X.XX - Sobrepeso"
8. SENÃO:
    Exibir: "IMC = X.XX - Obesidade"
9. Encerra algoritmo;
'''

peso = float(input("Digite seu peso em kg (ex.: 68.5):"))
altura = float(input("Digite sua altura em metros (ex.: 1.65):"))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Classificação
if imc < 18.5:
    categoria = "Magreza"
elif imc < 25:      #já sabemos que é >= 18.5 aqui
    categoria = "Normal"
elif imc < 30:      #já sabemos que é >= 25 aqui
    categoria = "Sobrepeso"
else:
    categoria = "Obesidade"

# Saída formatada
print(f"IMC = {imc:.2f} - {categoria}")

