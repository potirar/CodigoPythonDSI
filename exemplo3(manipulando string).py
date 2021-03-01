#manipulando string

texto = 'Técnico em Desenvolvimento de Sistemas'
print(texto)

#EXEMPLO DE FATIAMENTO DO CONTEÚDO

print(texto[3])
print(texto[0:15])

#STRING

print(len(texto)) #conta a quantidade de caractere
print(texto.upper()) #escreve tudo em maiúsculo
print(texto.lower()) #escreve tudo em minúsculo
print(texto.split()) #escreve em espaço com índice
print(texto.capitalize()) #escreve a primeira letra maiúscula
print(texto.replace('Sistemas','Internet')) #TROCA AS PALAVRAS
