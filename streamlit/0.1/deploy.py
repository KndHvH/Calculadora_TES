import streamlit as st

def main():
    html_temp = """ <div style ="background-color:blue;padding:13px">
                      <h1 style = "color:white;text-align:center;">Ferramentas Comerciais</h1>
                    </dic>
                """

    st.markdown(html_temp, unsafe_allow_html=True)

    # começo calc tes
    tes = 'test'
    st.header('Calculadora TES')

    opcoes = ['Selecione a Operação', "Venda Normal", "Amostra", "Doação", "Entrega futura de venda",
              "Entrega futura Remessa", "Demonstração", "Saida Troca",
              "Venda por conta e ordem", "Simples remessa"]

    checkbox = st.selectbox('', opcoes)

    operacao = numero_operacao(checkbox)

    if operacao != 0:

        if operacao == 9:
            tes = 521
        elif operacao == 6:
            a = st.checkbox('Produto para Demonstração em evento')
            if a:
                tes = 955
            else:
                tes = 956
        elif operacao == 2:
            tes = 527
        else:
            ipi = st.checkbox("Produto Com IPI", value=False, )

            if operacao == 4:
                if ipi:
                    tes = 505
                else:
                    tes = 537
            elif operacao == 8:
                if ipi:
                    tes = 522
                else:
                    tes = 540
            else:
                estado = st.checkbox("O cliente é de SP", value=False, )

                cnpj = st.checkbox("O cliente é pessoa juridica", value=False)

                contribuinte = False

                if cnpj:
                    contribuinte = st.checkbox("O cliente é contribuinte", value=False)

                lado = lado_tabela(estado, contribuinte)

                if operacao == 5:
                    if lado == 'a':
                        tes = 504
                    else:
                        tes = 949
                else:
                    fund = 0
                    choice = 1
                    if cnpj:
                        choice = st.number_input('Digite a origem do Produto:', min_value=1, max_value=6, value=1,
                                                 step=5)
                    if estado and cnpj:
                        options = ('Nenhum dos dois', 'Fapesp', 'FFM')
                        radio = st.radio('Cliente é Fapesp ou FFM?', options, index=0)

                        fund = fs(radio)

                    if operacao == 1:
                        if lado == 'a':
                            if fund == 1 and choice == 6:
                                if ipi:
                                    tes = 554
                                else:
                                    tes = 533
                            elif fund == 2:
                                if ipi:
                                    tes = 565
                                else:
                                    tes = 560
                            elif ipi:
                                tes = 501
                            else:
                                tes = 535
                        else:
                            if ipi:
                                tes = 948
                            else:
                                tes = 947
                    elif operacao == 3:
                        if lado == 'a':
                            if fs == 2:
                                tes = 928
                            elif ipi:
                                tes = 924
                            else:
                                tes = 925
                        else:
                            if ipi:
                                tes = 951
                            else:
                                tes = 950
                    else:
                        if fs == 1 and choice == 1:
                            tes = 544

                        if ipi == 0:
                            if fs == 2 or (fs == 1 and choice == 6):
                                tes = 550
                            tes = 900

                        else:
                            if fs == 2:
                                tes = 555
                            else:
                                tes = 544

        if st.button("Verificar"):
            b = f'TES: {tes}'
            st.info(b)
            # final calc tes


# inicio funcoes calc tes

def fs(radio):
    if radio == 'Fapesp':
        return 1
    elif radio == 'FFM':
        return 2
    return 0


def lado_tabela(sp, contr):
    if sp or contr:
        return 'a'
    return 'b'


def numero_operacao(txt):
    if txt == 'Selecione a Operação':
        x = 0
    elif txt == 'Venda Normal':
        x = 1
    elif txt == 'Amostra':
        x = 2
    elif txt == 'Doação':
        x = 3
    elif txt == 'Entrega futura de venda':
        x = 4
    elif txt == 'Entrega futura Remessa':
        x = 5
    elif txt == 'Demonstração':
        x = 6
    elif txt == 'Saida Troca':
        x = 7
    elif txt == 'Venda por conta e ordem':
        x = 8
    elif txt == 'Simples remessa':
        x = 9
    return x

    # final funcoes calc tes


if __name__ == '__main__':
    main()