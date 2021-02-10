from os import system
from time import sleep
turma = list()
aluno = {}

for i in range(0,2):
    aluno['nome'] = str(input('Informe o nome do aluno:')).title()
    aluno['nota1'] = float(input(f"Informe a nota 1 de {aluno['nome']}: "))
    aluno['nota2'] = float(input(f"Informe a nota 2 de {aluno['nome']}: "))
    aluno['nota3'] = float(input(f"Informe a nota 3 de {aluno['nome']}: "))
    aluno['média'] = (aluno["nota1"] + aluno["nota2"] + aluno["nota3"]) /3

    turma.append(aluno.copy())
    aluno.clear

print('\n')

for itens in turma:
    for chave, valor in itens.items(): # .items() -- retorna a chave e os valores
        if chave == "nome":
            print(f"Aluno(a) {valor}", end="")
        if chave == "média":
            print(f" teve a média = {valor:.2f}")

