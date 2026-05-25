
import sqlite3
conexao = sqlite3.connect('meu_sistema.db')
cursor = conexao.cursor()

comando_ddl = """
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    email TEXT UNIQUE NOT NULL
);
"""

cursor.execute(comando_ddl)
print("Estrutura da tabela criada com sucesso usando DDL!")
cursor.execute("""
INSERT INTO usuarios (nome, idade, email)
VALUES ('Mariana Costa', 26, 'mariana.costa@email.com')
""")
cursor.execute("""
INSERT INTO usuarios (nome, idade, email)
VALUES ('Rodrigo Santos', 34, 'rodrigo.santos@email.com')
""")
conexao.commit()
print("Dados gravados com sucesso!")

conexao.close()
print("Conexão com o banco fechada com segurança.")