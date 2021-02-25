#manipulação de lista e função
lista = []
#exemplo 1:
for cont in range(20):
    lista.append(cont)
print(lista)

#exemplo2: list comprehension
numero = [cont **2 for cont in range(20)]
print(numero)

#exemplo 4: funções anônimas\ lambda

soma = lambda x, y: x+y
soma(4,5)
print(soma(4,5))

#exemplo 4.1 - MAP

dobro = list(map(lambda x: x*2,lista))
print(dobro)
#exemplo 4.2 - FILTER
