produtos = [
    "carne 1 kg",9.00,
    "leite",3.98,
    "café",4.54,
    "Açúcar",2.75,
    "azeite",16.78,
    "Arroz 5kg",21.87
]

print("-"*40)

print(f"{'Lista de compras':^40}")

print("-"*40)


for indice,itens in enumerate(produtos):

    if indice % 2 == 0:
        print(f"{itens:.<30}", end="")

    else:
        print(f"{itens:>8}")

print("-"*40)