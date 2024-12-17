import mysql.connector
import os

# CONFIGURANDO O BANCO DE DADOS
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    database="meu_banco"
)
cursor = conn.cursor()


# Função CREATE: Criar usuário
def criar_usuarios(nome, email):
    sql = "INSERT INTO usuarios (nome, email) VALUES (%s, %s)"
    valores = (nome, email)
    cursor.execute(sql, valores)
    conn.commit()
    print(f"Usuário {nome} criado com sucesso!")


# Função READ: Ler o(s) usuário(s)
def ler_usuarios():
    sql = "SELECT * FROM usuarios"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for usuario in resultados:
        print(usuario)


# Função UPDATE: Atualizar o usuário
def atualizar_usuario(id_usuario, novo_nome, novo_email):
    sql = "UPDATE usuarios SET nome = %s, email = %s WHERE id = %s"
    valores = (novo_nome, novo_email, id_usuario)
    cursor.execute(sql, valores)
    conn.commit()
    print(f"Usuário de ID {id_usuario} atualizado com sucesso!")


# Função DELETE: Excluir o usuário
def delete_usuario(id_usuario):
    sql = "DELETE FROM usuarios WHERE id = %s"
    cursor.execute(sql, (id_usuario,))
    conn.commit()
    print(f"Usuário de ID {id_usuario} excluído com sucesso!")


# Exemplo de uso das funções
# Criando novos usuários
criar_usuarios("Pedro Braga", "pedrobraga@email.com")
criar_usuarios("Kamilly Ferreira", "kamillyferreira@email.com")
criar_usuarios("debora","debora@gmail.com")

# Lendo os usuários
ler_usuarios()

# Atualizando o usuário (supondo que o id do usuário seja 1)
atualizar_usuario(1, "Pedro Andrade", "pedroandrade@gmail.com")
atualizar_usuario(1, "teste", "teste@gmail.com")
atualizar_usuario(1, "isabela", "isabela@gmail.com")

# Deletando um usuário (supondo que o id do usuário seja 2)
delete_usuario(2)
delete_usuario(3)
delete_usuario(4)


# Lendo novamente os usuários
ler_usuarios()

# Fechando a conexão
cursor.close()
conn.close()
