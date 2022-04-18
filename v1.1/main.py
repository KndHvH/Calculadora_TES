from funcoes import *

#se é dentro do estado de SP (1 ou 0)
estado = int(input("Estado: "))

#se é contribuinte ou não (1 ou 0)
contribuinte = int(input("Contribuinte: "))
origem = 1

if contribuinte == 1:
    # origem produto (1 ou 6)
    origem = int(input("Origem produto: "))

    #fapesp ou ffm (0,1,2) (nao,fapesp,ffm)
    fs = f()

#produto com ou sem IPI (1 ou 0)
ipi = int(input("IPI: "))

lado = lado_tabela(estado,contribuinte)




