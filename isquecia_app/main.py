import mysql.connector
# Importando a função de conexão que criamos no passo anterior
from database import conectar_banco 

def cadastrar_usuario(nome, email, senha):
    conexao = conectar_banco()
    if conexao:
        try:
            cursor = conexao.cursor()
            
            # DESAFIO 1: Escreva o comando SQL de inserção (DML).
            # Lembre-se de usar %s como espaço reservado para evitar injeção de SQL.
            # Exemplo: "INSERT INTO nome_da_tabela (coluna1, coluna2) VALUES (%s, %s)"
            sql = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
            
            # DESAFIO 2: Coloque as variáveis (nome, email, senha) na mesma ordem do seu comando SQL
            valores = (nome, email, senha)
            
            cursor.execute(sql, valores)
            conexao.commit() # Salva definitivamente as alterações no banco
            
            print(f"\n✅ Sucesso! Usuário '{nome}' cadastrado no sistema TDAH.")
            
        except mysql.connector.Error as erro:
            print(f"\n❌ Erro ao cadastrar no banco de dados: {erro}")
        finally:
            # Fechando as portas por segurança
            cursor.close()
            conexao.close()

def menu_principal():
    while True:
        print("\n" + "="*30)
        print("🚀 SISTEMA DE APOIO TDAH")
        print("="*30)
        print("1. Cadastrar Usuário")
        print("2. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '1':
            print("\n--- NOVO CADASTRO ---")
            nome = input("Digite o nome do usuário: ")
            email = input("Digite o email do usuário: ")
            senha = input("Digite a senha do usuário: ")
            
            # DESAFIO 3: Use a função input() do Python para perguntar e guardar 
            # o nome, o email e a senha digitados pelo usuário no terminal.
            # nome_digitado = input("Digite ...")
            
            
            # DESAFIO 4: Após capturar os inputs, chame a função cadastrar_usuario()
            # passando as três variáveis que você acabou de criar.
            
            
        elif opcao == '2':
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("\n⚠️ Opção inválida. Tente novamente.")

# Ponto de partida do script
if __name__ == "__main__":
    menu_principal()