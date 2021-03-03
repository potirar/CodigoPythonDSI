from funcionario import Funcionario

f1 = Funcionario('Roberto','Padeiro',1100)
f1.relatorio()

f2 = Funcionario('Alberto','Cozinheiro')
f2.nome ='Jorge'
print(f"O salário de {f2.nome} é R$ {f2.sal}")