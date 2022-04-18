def f():
    #pergunta se é fapesp (1,0)
    fapesp = int(input("Fapesp? "))
    if fapesp == 0:
        # pergunta se é ffm (1,0)
        ffm = int(input("Ffm? "))

        if ffm==1:
            return 2
        else:
            return 0
    else:
        return 1


def lado_tabela(sp, contr):
    if sp == 1 or contr == 1:
        return 'a'
    return 'b'


def notas():
    return int(input(
        "<1> - Venda Normal\n" +
        "<2> - Amostra\n" +
        "<3> - Doação\n" +
        "<4> - Entrega futura de venda\n" +
        "<5> - Entrega futura Remessa\n" +
        "<6> - Demonstracao\n" +
        "<7> - Saida Troca\n" +
        "<8> - Venda por conta e ordem\n" +
        "<9> - Simples remessa" +
        "\nDigite o numero equivalente a operacao:\n" \
         ))

def decisao(operacao,lado,ipi):
    if operacao == 1:
        return op1(lado,ipi)

    else:
        return 'ERROR'

def op1(lado,ipi):
    if lado == 'a':
        if ipi == 1:
            return 501
        else:
            return 535
    else:
        if ipi == 1:
            return 948
        else:
            return 947