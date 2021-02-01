preco1 = float(input("Qual o valor do produto:R$"))
preco2 = float(input("Qual o valor do produto: R$"))
preco3 = float(input("Qual o valor do produto:R$"))

ValorTotal = (preco1+preco2+preco3)
print("O total das suas compras é: ", ValorTotal)
Desconto = ValorTotal*0.2
print("Seu desconto é: ",Desconto)
valorPagar = ValorTotal - Desconto
print("O seu valor é:R$",valorPagar)