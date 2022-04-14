from funcoes import *

tes = 'ERRO'

#se é dentro do estado de SP (1 ou 0)
estado = int(input("Estado: "))

#se é contribuinte ou não (1 ou 0)
contribuinte = int(input("Contribuinte: "))

#produto com ou sem IPI (1 ou 0)
ipi = int(input("IPI: "))

#origem produto (1 ou 6)
origem = int(input("Origem: "))

#chamando a funcao pra definir o lado da tabela
lado = lado_tabela(estado,contribuinte)

#chamando a funcao pra definir tipo de operacao
operacao = notas()

tes = decisao(operacao,lado,ipi,origem)

print("TES:",tes)
