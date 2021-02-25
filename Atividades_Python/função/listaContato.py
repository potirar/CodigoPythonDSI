lista = []
def listaNomes():
    while True:
        lista.append(str(input("Insira um contato na sua agenda: ")).title())

        op = str(input("Deseja continuar s/n: ")).lower()
        if op == "n":
            break

def excluiNomes():
    for indice, nomes in enumerate(lista):
        print(f"{indice}:{nomes}")
    posicao = int(input("Qual a posição da pessoa que você deseja excluir? "))

    print("Foi excluído com sucesso! \n")
    lista.pop(posicao)

while True:
    print("1. Insira nome do contato:")
    print("2. Excluir nome do contato:")
    print("3. Sair")

    op = int(input("Qual a opção você deseja? "))
    if op == 1:
        listaNomes()
    elif op == 2:
        excluiNomes()
    elif op == 3:
        break