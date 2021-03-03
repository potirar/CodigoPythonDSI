#manipulação de lista e função
lista = []
#exemplo 1:
for cont in range(20):
    lista.append(cont)
print(lista)

#exemplo2: list comprehension
numero = [cont **2 for cont in range(20)]
print(numero)

#exemplo 4: funções anônimas\lambda

soma = lambda x, y: x+y
soma(4,5)
print(soma(4,5))

#exemplo 4.1 - map()

dobro = list(map(lambda x: x*2,lista))
print(dobro)

#exemplo 4.2 - FILTER

valores = list(range(20,61))
print(valores)

pares = list(filter(lambda num:num % 2 == 0,valores))
'''print("Os números pares são: \n",pares)''' #pode ser essa formatação ou com format :')
print(f'Os números pares são: {pares}')
