import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'turma_sistema'
)

cod = int(input("Informe o código da disciplina: "))
nome = str(input("Informe um nome para a disciplina: "))
desc = str(input("Informe uma descrição para a disciplina: "))
ch = int(input("Informe a carga horária: "))

comando = "insert into disciplina values(%s,%s,%s,%s)" #entra nos itens do banco de dado

valores = (cod,desc,nome,ch)

consulta = conexao.cursor() #criando a variavel consulta

consulta.execute(comando,valores) #executando o banco

conexao.commit() #gravando dados no bd

print(consulta.rowcount,"linha(s) inserida com sucesso!")

conexao.close()

