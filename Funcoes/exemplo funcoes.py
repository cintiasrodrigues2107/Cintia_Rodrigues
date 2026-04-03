# def = funções
# Estrutura básica: é um bloco de situações específicas que pode ser reutilizável;
# Funções tem que ter nomes claros;
# Funções pequenas, para não juntar todas na mesma;
# Tem que ter uma responsabilidade;


#Funcao para colocar saudação:
def saudacao():
    print("Olá, aluno!")
    
saudacao()

# Função com mais uma variável:

def saudacao(nome):
    print(f"Olá, {nome}!")
    
saudacao("Cintia")
saudacao("Alexandre")
saudacao("Ciclano")

#Função Multiplos parâmetros:

def soma(a, b, c):
    soma = a + b + c
    print(soma)

soma(2, 5, 8)

# Funcao de Return = ela só executa e retorna para usar no código depois:

def soma(a, b):
    soma = (a + b)
    return soma

resultado = soma(5, 3)
print(resultado)

#Função para calculo de media:
def media(a, b, c):
    media = (a + b + c) / 3
    return media
