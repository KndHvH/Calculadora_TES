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