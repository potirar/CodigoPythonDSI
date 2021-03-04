#ANALISE DE ERRO/TRATAMENTO DE ERRO
num1= int(input("Informe um valor númerico: "))
num2 = int(input("Informe outro um valor númerico: "))

try:
    resultado = num1/num2
except Exception as erro:
    print(f"ERRO NO SISTEMA: {erro.__class__}")
else:
    print(f"O resultado é {resultado}")
