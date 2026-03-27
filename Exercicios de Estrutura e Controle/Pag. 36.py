'''
# Classificação de Temperatura:
Algoritmo: 
1. Peça para usuária digitar uma temperatura atual;
2. Classifique conforme a tabela
    <10°C = Muito Frio
    10 a 24°C = Agradável
    25 a 30°C = Quente
    30°C = Muito Quente
3. Imprima a classificação
'''

temperatura = float(input("Digite a temperatura atual em °C (ex.: 27.5°C):"))

#Classificação:

if temperatura < 10:
    clima = "Muito Frio"
elif temperatura < 24:
    clima = "Agradável"
elif temperatura < 30:
    clima = "Quente"
else:
    clima = "Muito Quente"

print(f"temperatura = {temperatura:.2f} - {clima}")
