nome = ''

while len(nome) <= 15: #len: conta a quantidade de caractere dentro do vetor
    nome = input('Informe seu nome:')
    print(f'O nome {nome} possui {len(nome)} caractere')
print('Esse nome atende aos requisitos, até próxima')
