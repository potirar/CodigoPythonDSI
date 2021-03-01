import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'ecommerce'
)


cod = int(input("Informe o código do produto: "))
nomeProd = str(input("Informe o nome do produto: "))
fornecedor = str(input("Informe o fornecedor do produto: "))
descricao = str(input("Informe a descrição do produto: "))
end = str(input("Informe o endereço da loja: "))
site = str(input("Informe o site do fabricante: "))

comando = 'insert into produto values(%s,%s,%s,%s,%s,%s)'

valor = (cod,nomeProd,fornecedor,descricao,end,site)

consulta = conexao.cursor()

consulta.execute(comando,valor)

conexao.commit()

print(consulta.rowcount,"Produto no carrinho. Finalize sua compra!")

conexao.close()