'''
# Dados = dados informados em um banco de dados;
# Informação = são baseados nos dados para gerar as informações;
# Conhecimento = é a interpretação das informações para gerar o conhecimento;
# Sabedoria = é a aplicação do conhecimento para tomar decisões e resolver problemas.
# Metadados = são dados sobre os dados, ou seja, informações que descrevem e contextualizam os dados, como sua origem, formato, estrutura e significado. 
    Eles ajudam a organizar, entender e utilizar os dados de forma mais eficiente.
    
# BD Relacional = é um tipo de banco de dados que organiza os dados em tabelas relacionadas entre si, permitindo consultas complexas e integridade referencial.
#Ex. Pense numa tabela de excel, com colunas e linhas, onde cada linha representa um registro e cada coluna representa um campo ou atributo do registro.

# BD Não Relacional = é um tipo de banco de dados que não utiliza tabelas relacionais, mas sim outros modelos de dados, como documentos, grafos ou colunas, para armazenar e gerenciar 
    os dados de forma mais flexível e escalável.
#Ex. Pense numa coleção de documentos JSON, onde cada documento representa um registro e cada campo representa um atributo do registro, 
    sem a necessidade de uma estrutura fixa ou relacionamentos entre os documentos.
    
#Arquitetura de BD = é a estrutura organizacional e o design de um banco de dados, que define como os dados são armazenados, acessados e gerenciados.

#Centralizada = é um modelo de arquitetura de banco de dados onde os dados são armazenados e gerenciados em um único local, geralmente em um servidor centralizado,
    e os usuários acessam os dados por meio de uma rede.
    
#Cliente-Servidor = é um modelo de arquitetura de banco de dados onde os dados são armazenados e gerenciados em um servidor centralizado, 
    e os usuários acessam os dados por meio de clientes que se conectam ao servidor.
    
#Distribuída = é um modelo de arquitetura de banco de dados onde os dados são armazenados e gerenciados em vários locais, 
    geralmente em servidores distribuídos, e os usuários acessam os dados por meio de uma rede.
    
#Replicada = é um modelo de arquitetura de banco de dados onde os dados são replicados em vários locais,
    geralmente em servidores distribuídos, para garantir a disponibilidade e a tolerância a falhas.
    
#Utilitarios = são ferramentas ou programas que auxiliam na administração, manutenção e otimização de um banco de dados,
    como ferramentas de backup, monitoramento, análise de desempenho e gerenciamento de usuários.  

#carregamento (ETL) = Carregamento de dados é o processo de transferir dados de uma fonte para um destino, geralmente em um banco de dados ou data warehouse,
    para que possam ser armazenados, processados e analisados de forma eficiente.

#Backup = é o processo de criar uma cópia de segurança dos dados de um banco de dados, para garantir a recuperação em caso de falhas, perda ou corrupção dos dados.

#Reorganização de arquivos = é o processo de reorganizar os arquivos de um banco de dados para melhorar o desempenho, reduzir a fragmentação e otimizar o uso do espaço em disco.

#SQL = é uma linguagem de consulta estruturada usada para gerenciar e manipular bancos de dados relacionais, permitindo a criação, leitura, atualização e exclusão de dados.
    é a linguagem que usamos para rodar o BD;

#Cuidar a versao do SQL, sempre a mais nova, para evitar problemas de compatibilidade e aproveitar os recursos mais recentes.

#Subconjuuntos de SQL = são partes específicas da linguagem SQL que se concentram em diferentes aspectos do gerenciamento de bancos de dados, 
# DDL (Data Definition Language), (select) - seleção de dados em um banco de dados, permitindo recuperar informações específicas com base em critérios definidos.
# DML (Data Manipulation Language) (insert, update, delete) - para manipular os dados em um banco de dados, permitindo inserir, atualizar e excluir registros em tabelas.
# DCL (Data Control Language) (create, alter, drop) - para criar, alterar e excluir objetos do banco de dados, como tabelas, índices e usuários.
# DCL (Data Control Language) (grant, revoke) - para conceder ou revogar permissões de acesso aos objetos do banco de dados, como tabelas, colunas e procedimentos armazenados.
# DTL (Data Transaction Language) (commit, rollback, begin) - para controlar as transações em um banco de dados, permitindo confirmar ou desfazer as operações realizadas em uma transação.

# BIGINT = é um tipo de dado numérico em bancos de dados que pode armazenar valores inteiros muito grandes, 
    geralmente com uma faixa de -9.223.372.036.854.775.808 a 9.223.372.036.854.775.807, dependendo do sistema de banco de dados utilizado.

# DECIMAL = é um tipo de dado numérico em bancos de dados que pode armazenar valores decimais com precisão e escala definidas, 
    permitindo representar números com casas decimais de forma precisa, como valores monetários ou medidas.

# FLOAT = é um tipo de dado numérico em bancos de dados que pode armazenar valores decimais com precisão variável,
    permitindo representar números com casas decimais de forma aproximada, mas com uma faixa de valores muito ampla, dependendo do sistema de banco de dados utilizado.
    
# VARCHAR (n) = é um tipo de dado em bancos de dados que pode armazenar cadeias de caracteres de comprimento variável,
    onde "n" representa o número máximo de caracteres que podem ser armazenados, permitindo armazenar textos de forma eficiente, sem ocupar espaço desnecessário.
    
# CHAR (n) = é um tipo de dado em bancos de dados que pode armazenar cadeias de caracteres de comprimento fixo,
    onde "n" representa o número de caracteres que serão armazenados, preenchendo com espaços em branco os caracteres restantes, 
    o que pode ser útil para armazenar dados com um formato específico ou para otimizar o desempenho em consultas.
    
    Libera a memória, pois só ocupa o espaço necessário para armazenar os caracteres, ao contrário do CHAR, que ocupa o espaço fixo definido por "n", 
    mesmo que a cadeia de caracteres seja menor.

# TEXT = é um tipo de dado em bancos de dados que pode armazenar grandes quantidades de texto, geralmente com uma capacidade de armazenamento muito maior do que os tipos VARCHAR ou CHAR,
    permitindo armazenar textos longos, como descrições, comentários ou artigos, sem a necessidade de definir um limite de caracteres específico.
    
# Diferença do TEXT e BIGTEXT = o tipo de dado TEXT é usado para armazenar grandes quantidades de texto, 
    enquanto o tipo de dado BIGTEXT é uma extensão do TEXT que pode armazenar ainda mais texto,
    geralmente com uma capacidade de armazenamento muito maior do que o TEXT, dependendo do sistema de banco de dados utilizado. 
    O BIGTEXT é útil para armazenar textos extremamente longos, como livros, documentos ou artigos extensos, que excedem a capacidade do tipo de dado TEXT.

# TIME = é um tipo de dado em bancos de dados que pode armazenar valores de tempo, geralmente no formato de horas, minutos e segundos,
    permitindo representar horários, durações ou intervalos de tempo de forma precisa e eficiente.
    
# BOOLEAN OU TINYINT = é um tipo de dado em bancos de dados que pode armazenar apenas dois valores: verdadeiro (true) ou falso (false),
    permitindo representar informações binárias ou de estado, como sim/não, ligado/desligado, ou presença/ausência, de forma simples e eficiente.

# TIMESTAMP = é um tipo de dado em bancos de dados que pode armazenar valores de data e hora, geralmente no formato de ano, mês, dia, hora, minuto e segundo,
    permitindo representar momentos específicos no tempo, como data de criação, data de atualização ou data de eventos, de forma precisa e eficiente.
    EX.: para converter a data e hora de um local para outro.

# ENUM = é um tipo de dado em bancos de dados que pode armazenar um conjunto de valores pré-definidos, permitindo representar informações categóricas ou enumeradas,
    como status, tipos ou categorias, de forma eficiente e fácil de usar, garantindo que os valores armazenados sejam limitados a um conjunto específico de opções.

# TIPOS DE CHAVE = são usados para identificar de forma única um registro em uma tabela de banco de dados, garantindo a integridade e a consistência dos dados.

# Chave Primária (Primary Key) = é um campo ou conjunto de campos que identifica de forma única cada registro em uma tabela, 
    garantindo que não haja registros duplicados e permitindo a criação de relacionamentos entre tabelas.
    EX.: em uma tabela de clientes, o campo "ID do Cliente" pode ser definido como chave primária, garantindo que cada cliente tenha um identificador único.
    (NÃO PODE REPETIR E SER NULO)
    (TODA PRIMARY KEY É UNIQUE, MAS NEM TODO UNIQUE É PRIMARY KEY.)
    (CADA TABELA DEVE TER UMA);
    
# Chave Unica (Unique Key) = é um campo ou conjunto de campos que também identifica de forma única cada registro em uma tabela,
    mas permite a existência de valores nulos, ou seja, pode haver registros sem um valor único, desde que não haja registros duplicados com valores não nulos.
    EX.: em uma tabela de usuários, o campo "Email" pode ser definido como chave única, garantindo que cada usuário tenha um endereço de email único, 
    mas permitindo que alguns usuários não tenham um endereço de email registrado (valor nulo).

# Chave Estrangeira (Foreign Key) = é um campo ou conjunto de campos em uma tabela que faz referência à chave primária de outra tabela,
    estabelecendo um relacionamento entre as duas tabelas e garantindo a integridade referencial dos dados.
    EX.: em uma tabela de pedidos, o campo "ID do Cliente" pode ser definido como chave estrangeira, 
    fazendo referência à chave primária "ID do Cliente" na tabela de clientes, permitindo associar cada pedido a um cliente específico.
    CORRELAÇÃO ENTRE DUAS TABELAS, PARA GARANTIR A INTEGRIDADE REFERENCIAL DOS DADOS.
    
# NOT NULL = é uma restrição em bancos de dados que indica que um campo não pode conter valores nulos, ou seja, deve sempre conter um valor válido,
    garantindo que os dados sejam completos e consistentes, e evitando a inserção de registros com campos vazios ou sem informações essenciais.
    (NÃO PODE SER NULO, MAS PODE SER VAZIO)

# DEFAULT = é uma restrição em bancos de dados que define um valor padrão para um campo, que será atribuído automaticamente 
    quando nenhum valor for especificado durante a inserção de um registro, garantindo que os dados tenham um valor consistente 
    e evitando a inserção de registros com campos vazios ou sem informações essenciais.
    (É O MEU PADRÃO)

# AUTO_INCREMENT = é uma propriedade em bancos de dados que permite que um campo seja automaticamente incrementado a cada nova inserção de registro,
    geralmente usado para chaves primárias, garantindo que cada registro tenha um identificador único e sequencial, 
    sem a necessidade de especificar manualmente o valor do campo durante a inserção.
    (ELE SEMPRE PEGA ULTIMO VALOR E INCREMENTA +1, PARA GARANTIR QUE CADA REGISTRO TENHA UM IDENTIFICADOR ÚNICO E SEQUENCIAL);

# CHECK = é uma restrição em bancos de dados que define uma condição que os valores de um campo devem satisfazer,
    garantindo que os dados inseridos sejam válidos e consistentes, e evitando a inserção de registros com valores inválidos ou fora do intervalo permitido.
    (É UMA CONDIÇÃO QUE OS VALORES DE UM CAMPO DEVEM SATISFAZER, PARA GARANTIR QUE OS DADOS INSERIDOS SEJAM VÁLIDOS E CONSISTENTES);
    
# COMMENT = é uma funcionalidade em bancos de dados que permite adicionar comentários ou descrições a campos, tabelas ou outros objetos do banco de dados,
    fornecendo informações adicionais sobre o propósito, uso ou significado dos dados, e facilitando a compreensão e 
    manutenção do banco de dados por parte dos desenvolvedores, administradores e outros usuários.


'''