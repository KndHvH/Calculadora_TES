
def lado_tabela(sp,contr):
    if sp == 1 or contr == 1:
        return 'a'
    return 'b'

def notas():
    return input(
        "<1> - Venda Normal\n" +
        "<2> - Amostra\n" +
        "<3> - Doação\n" +
        "<4> - Entrega futura de venda\n" +
        "<5> - Entrega futura Remessa\n" +
        "<6> - FFM\n" +
        "<7> - Fapesp\n" +
        "<8> - Demonstracao\n" +
        "<9> - Saida Troca\n" +
        "<10> - Saida Troca FFM/Fapesp" +
        "<11> - Venda por conta e ordem\n" +
        "<12> - Simples remessa" +
        "\nDigite o numero equivalente a operacao:\n" \
         )

def decisao(operacao,lado,ipi,origem):

    if operacao == 1:
        if lado=='a':
            if ipi == 1:
                return '501'
            else:
                return '535'
        else:
            if ipi==1:
                return '948'
            else:
                return '947'

'''    if operacao == 2:

    if operacao == 3:

    if operacao == 4:

    if operacao == 5:

    if operacao == 6:

    if operacao == 7:

    if operacao == 8:

    if operacao == 9:

    if operacao == 10:

    if operacao == 11:

    else:'''