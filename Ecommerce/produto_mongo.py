from pymongo import MongoClient

produto = MongoClient('localhost',27017)

banco = produto.ecommerce

colecao = banco.produtos

while True:
    print(f"{' PRODUTO ':-^40}")
    op = int(input('''
        1. Insira um produto
        2. Exiba o produto
        3. Excluir o produto
        4. Sair

        \n\nQual a sua escola: '''))

    if op == 1:
        
        codigo = int(input("Informe o código do produto: "))
        nomeProd = str(input("Informe o nome do produto: ")).title()
        fornecedor = str(input("Informe o fornecedor do produto: ")).capitalize()
        descricao = str(input("Informe a descrição do produto: ")).capitalize()
        endereco = str(input("Informe o endereço do fornecedor: "))
        site = str(input("Informe o site do fabricante: ")).lower()

        colecao.insert_one({

            'codigo':codigo,
            'nomeProd':f'{nomeProd}',
            'fornecedor':f'{fornecedor}',
            'descricao':f'{descricao}',
            'endereco':f'{endereco}',
            'site':f'{site}'
        })
        print("Produto inserido no carrinho. Finalize as suas compras!\n")

    elif op == 2:
        print(f"{'PRODUTOS':-^40}\n")
        for item in colecao.find():
            print(f"{item['nomeProd']} : {item['descricao']} - {item['fornecedor']}")
        print("-"*40)

    elif op == 3:
        escolha = int(input("Escolha um código: "))
        resultado = colecao.delete_one({
            'codigo':escolha
        })

    elif op == 4:
        break
