produto = { # recorre a um dicionário
    
    'Salgado':4.90,
    'Suco':3.00,
    'Refrigerante':4.00,
    'Hamburguer':7.20,
    'Doce':2.20

}

print("-"*48)

print(f"{'Lanchonete':<32}{'Preço'}")
print("-"*48)


for i,itens in produto.items():
    print(f'{i:.<30}R${itens:>5}')
   