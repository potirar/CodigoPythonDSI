from agregacao import Cliente
from agregacao import Conta

c1 = Cliente('Maurício Sousa Filho','98 987412104','126.358.789-41','Rua das Margaridas, nº 35, Bairro Catarinão')
conta1 = Conta(1236,c1,1100,2000)

print(f"O Cliente {conta1.titular.nome} passui o saldo R$ {conta1.saldo} e mora no endereço {conta1.titular.endereco}. Seu telefone para contato é {conta1.titular.telefone} e um limite para compras de R$ {conta1.limite}\n")