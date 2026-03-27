'''
# Notas:
Algoritimo:
1. Solicite ao usuario uma nota (0 a 10);
2. Classifique:
    <5 = "Reprovado"
    5 a 6.9 = "Recuperação"
    7 a 8.9 = "Aprovado"
    9 a 10 = "Aprovado com Excelência"
3. Imprima a classificação;
'''

nota = float(input ("Digite a nota do aluno '0 a 10':"))

#Classificação:

if nota < 5:
    situacao = "Reprovado"
elif nota < 6.9:
    situacao = "Recuperação"
elif nota < 8.9:
    situacao = "Aprovado"
else:
    situacao = "Aprovado com Excelência"

print(f"nota final = {nota:.2f} - {situacao}")
