pessoas = {
"nome":"Mariana",
"idade":29,
"bairro":"Cidade Operária"
}
print(pessoas)

print(f"Olá {pessoas['nome']}, você tem {pessoas['idade']} anos e mora no bairro {pessoas['bairro']}\n\n")
#print(type(pessoas))

print(pessoas.keys()) #exibindo as chaves
print(pessoas.values()) #exibindo as chaves
print(pessoas.items()) #exibindo os itens (chave e valor)
