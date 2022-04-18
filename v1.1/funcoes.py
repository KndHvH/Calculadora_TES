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

def decisao(operacao,lado,ipi,fs,origem):
    count = 1
    for iop in (op1,op2,op3,op4,op5,op6,op7,op8,op9):
        if operacao == count:
            return iop(lado,ipi,fs,origem)
        else:
            count += 1
def op1(lado,ipi,fs,origem):

    if lado == 'a':
        if fs == 1 and origem == 6:
            return 533
        if fs == 2:
            if ipi == 1:
                return 565
            else:
                return 560
        if ipi == 1:
            return 501
        else:
            return 535
    else:
        if ipi == 1:
            return 948
        else:
            return 947

def op2(lado,ipi):
     return 527

def op3(lado,ipi):
    if lado == 'a':
        if ipi == 1:
            return 924
        else:
            return 925
    else:
        if ipi == 1:
            return 951
        else:
            return 950

def op4(lado,ipi):
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
