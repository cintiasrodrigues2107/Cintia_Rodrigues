#Leia um número como string e imprima o seu tipo antes e depois de converter para int.

número = input("Digite um número: ")
print("Tipo antes da conversão:", type (número))

número = int(número)
print("Tipo depois da conversão:", type(número))

#########################################################

n_str = "10"
print(type(n_str))
n_int = int(n_str)
print(type(n_int))
