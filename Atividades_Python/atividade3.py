taxa = 0.2
preco1 = float(input("Qual o valor do 1º produto:R$"))
preco2 = float(input("Qual o valor do 2º produto: R$"))
preco3 = float(input("Qual o valor do 3º produto:R$"))

ValorTotal = (preco1+preco2+preco3)
print("O total das suas compras é: ", ValorTotal)

Desconto = ValorTotal*taxa
print("Seu desconto é: ",Desconto)

valorPagar = ValorTotal - Desconto
print("O seu valor é:R$",valorPagar)