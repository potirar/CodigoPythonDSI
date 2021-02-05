pessoas = ('Carlos','Mario','Luíza','Felipe') #toda tupla é representada por parênteses

print(type(pessoas))
print(pessoas)

#pessoas[1] = 'Ronaldo --em tuplas não pode-se modificar itens já declarados
print(pessoas[1])

for i in pessoas: #i será meu contador
    print(i)

print('Luíza está na posição',pessoas.index('Luíza')) #index serve para mostrar a posição da variavel

for indice,i in enumerate(pessoas): #enumerate serve para enumerar itens
    print(f'{indice:.<20}{i}') #':<tam' alinhamento

