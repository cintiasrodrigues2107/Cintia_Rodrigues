#6. Faça uma calculadora simples contendo as operações: soma, subtração, divisão e multiplicação. 
# Solicite ao usuário que informe dois número e que informe também a operação que deseja realizar (+, -, /, *) e depois exiba o resultado.


# 1. Solicita os números ao usuário (usamos float para permitir decimais)
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# 2. Solicita qual operação deseja realizar
operacao = input("Digite a operação desejada (+, -, *, /): ")

# 3. Estrutura de controle para decidir qual conta fazer
if operacao == '+':
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")

elif operacao == '-':
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")

elif operacao == '*':
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")

elif operacao == '/':
    # Verificação importante: não existe divisão por zero
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
    else:
        print("Erro: Não é possível dividir por zero!")

else:
    print("Operação inválida. Tente novamente usando +, -, * ou /.")