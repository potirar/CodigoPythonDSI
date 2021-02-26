#estabelecendo a conexão
from pymongo import MongoClient

#pprint é uma biblioteca para tornar mais amigável a saída do console
from pprint import pprint

#conectando o servidor local
#client = pymongo.MongoClient("mongodb://localhost:27017/")

cliente = MongoClient('localhost',27017)

banco = cliente.santander #criando um banco

colecao = banco.clientes #criando collections

while True:
    print(f"{' MENU ':-^40}")
    op = int(input('''
        1. inserir dados
        2. exibir dados
        3. excluir dados
        4. sair

        Qual sua escolha: ''')) #Após o input permite formatar o texto.

   
    if op == 1:
        
        cpf = int(input("Informe o seu CPF: "))
        nome = str(input("Informe o seu Nome: ")).title()
        sexo = str(input("Informe seu sexo:(m/f): ")).lower()
        salario = float(input("Informe o seu salário: "))
        endereco = str(input("Informe o seu endereço: ")).title()

#criando dados na collection
        colecao.insert_one({
            'cpf':cpf,
            'nome':f'{nome}',
            'sexo':f'{sexo}',
            'salario':salario,
            'endereco':f'{endereco}'
        })
        print('\nDados inseridos com sucesso!!\n')

    elif op == 2:
       print(f"{'Exibindo os dados':-^40}\n")
       for item in colecao.find():
           print(f"{item['nome']}, possui salário de R$ {item['salario']} e reside no endereço {item['endereco']} e seu cpf é {item['cpf']}\n")
        
    elif op == 3:
        escolha = int(input("Qual o cpf você deseja excluir: "))
        resultado = colecao.delete_one({
            'cpf':escolha
        })
        print("Clientes excluídos: ",resultado.deleted_count)#contando quantos itens foram excluídos.
    elif op == 4:
        break