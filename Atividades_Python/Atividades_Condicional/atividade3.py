produto1 =float(input('Informe o valor do produto 1:'))
produto2 =float(input('Informe o valor do produto 2:'))
produto3 =float(input('Informe o valor do produto 3:'))
'''
if produto1 < produto2 < produto3:
    print('Você escolheu o produto 1 e ganhou desconto!!')

elif produto2 < produto3 < produto1:
    print('Você escolheu o produto 2 e ganhou desconto!!')

elif produto3 < produto2 < produto1:
    print('Você escolheu o produto 3 e ganhou desconto!!')
'''
print('Dos 3 produtos mais baratos é {}'.format(min(produto1,produto2,produto3)))
