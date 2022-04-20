from funcoes import *

print("------------------------------")
print("Calculadora TES - ver 1.1")
print("Digite 1 para respoder \"sim\"")
print("Digite 0 para respoder \"nao\"")

while True:
    print("------------------------------")

    estado = bool("Cliente é de SP?: ")

    cpf = bool("É pessoa fisica?: ")

    contribuinte = 0

    if cpf == 0:
        contribuinte = bool("É contribuinte?: ")


    origem = 1
    fs = 0

    if contribuinte == 1:
        while True:
            origem = input("Digite a origem do produto (1/6): ")
            x = loop(origem)
            if x == '6' or x == '1':
                origem = int(origem)
                break
            else:
                print("Favor responder com 6 ou 1.")

        if estado == 1:
            #fapesp ou ffm (0,1,2) (nao,fapesp,ffm)
            fs = f()


    ipi = bool("Produto tem IPI?: ")

    lado = lado_tabela(estado,contribuinte)

    operacao = 1
    diff = bool("Operacao diferente de venda normal? ")
    if diff != 0:
        while True:
            operacao = notas()
            #PAREI AQUI
            if operacao.isnumeric():
                if operacao >= 1 and operacao <10:
                    break
            print("Favor responder com numeros entre 1 e 9.")


    demonstracao=0
    if operacao == 6:
        demonstracao = bool("Produto para demonstração em evento?: ")


    tes = decisao(operacao,lado,ipi,fs,origem,demonstracao)

    print("------------------------------")
    print("TES:",tes)
    print("------------------------------")
    x = bool("Deseja calcular novamente?: ")
    if x != 1:
        break


