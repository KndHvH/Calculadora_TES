from funcoes import *

#se é dentro do estado de SP (1 ou 0)
estado = int(input("É de SP?: "))

#é pessoa fisica? (1 ou 0)
cpf = int(input("tem CPF: "))

contribuinte = 0

if cpf == 0:
    # se é contribuinte ou não (1 ou 0)
    contribuinte = int(input("Contribuinte: "))


origem = 1

if contribuinte == 1:
    # origem produto (1 ou 6)
    origem = int(input("Origem produto: "))

    #fapesp ou ffm (0,1,2) (nao,fapesp,ffm)
    fs = f()

#produto com ou sem IPI (1 ou 0)
ipi = int(input("Valor IPI: "))
if ipi>0:
    ipi = 1

lado = lado_tabela(estado,contribuinte)

operacao = notas()


tes = decisao(operacao,lado,ipi)

print(tes)


