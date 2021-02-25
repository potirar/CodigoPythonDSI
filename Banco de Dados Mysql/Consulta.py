import pymysql

#estabelecer a conexão

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'turma_sistema'
)

#permite interagir com bd [nome_bd.cursor()]
consulta = conexao.cursor()

sql = "select * from aluno"
sql = "selec * from where carga_horaria disciplina >=200"

consulta.execute(sql) #consultando o banco todo
for itens in consulta:
   print(itens)

#personalizando a consulta

resultado = consulta.fetchall() #busca todos os itens de fprma mais organizada dentro da tabela

for itens in resultado: #consultar dados dentro do bd
    print(f"Olá {itens[1]} você mora no bairro {itens[4]}")

for itens in resultado:
    print(f"A disciplina {itens[1]} e tem a carga horária de {itens[3]}")

    conexao.close() #encerrando a conexão

