# Leia tempo em segundos (int). Converta para minutos inteiros com //= 60 e depois use %= 60 para obter segundos restantes.

tempo = int(input("Quantos segundos: "))
converte = tempo
converte //= 60
print(converte) 

resto = tempo
resto %= 60
print(resto)