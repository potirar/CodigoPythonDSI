from associacao import Celular
from associacao import Pessoa

smartphone = Celular('Xiaomi',1500)

p1 = Pessoa('Carlos',34,'Rua 71 Cidade Operária')

print(f'{p1.nome} mora no endereço {p1.endereco} e tem {p1.idade} anos')

p1.celular = smartphone

print(f"{p1.nome} possui um celular da marcar {p1.celular.marca} e custou R$ {p1.celular.valor}")