from funcoes import *

print("------------------------------")
print("Calculadora TES - ver 1.1")
print("Digite 1 para respoder \"sim\"")
print("Digite 0 para respoder \"nao\"")
x=1
while x==1:
    print("------------------------------")

    #se é dentro do estado de SP (1 ou 0)
    estado = int(input("Cliente é de SP?: "))

    #é pessoa fisica? (1 ou 0)
    cpf = int(input("É pessoa fisica?: "))

    contribuinte = 0

    if cpf == 0:
        # se é contribuinte ou não (1 ou 0)
        contribuinte = int(input("É contribuinte?: "))


    origem = 1
    fs = 0
    if contribuinte == 1:
        # origem produto (1 ou 6)
        origem = int(input("Digite a origem do produto (1/6): "))
        if estado == 1:
            #fapesp ou ffm (0,1,2) (nao,fapesp,ffm)
            fs = f()

    #produto com ou sem IPI (1 ou 0)
    ipi = int(input("Produto tem IPI?: "))
    if ipi>0:
        ipi = 1

    lado = lado_tabela(estado,contribuinte)

    operacao = 1
    diff = int(input("Operacao diferente de venda normal? "))
    if diff != 0:
        operacao = notas()

    demonstracao=0
    if operacao == 6:
        demonstracao = int(input("Produto para demonstração em evento?: "))


    tes = decisao(operacao,lado,ipi,fs,origem,demonstracao)

    print("------------------------------")
    print("TES:",tes)
    print("------------------------------")
    x = int(input("Deseja calcular novamente?: "))


