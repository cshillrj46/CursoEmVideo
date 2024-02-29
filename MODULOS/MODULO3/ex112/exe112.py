from utilidadeCeV import moeda
from utilidadeCeV import dado

preco = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(preco, 20, 12)