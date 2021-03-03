from conta import Conta2
'''
contaPessoal = Conta(1123,"Carlos José Silva Carneiro",500)

contaPessoal.deposito(100)
contaPessoal.getSaldo()

contaPessoal.saque(100)
contaPessoal.getSaldo()
'''
minhaConta = Conta2(529,"Sergio Mota Filho",700)
print(minhaConta.saldo)

minhaConta.saldo = 600
print(minhaConta.saldo)