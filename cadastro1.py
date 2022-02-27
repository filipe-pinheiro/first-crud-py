from cadastro2 import cadastro, sair, deletar
from terminaltables import AsciiTable

cabecalho = '''
PROJETO DE CADASTRO DE ITENS DE UMA LOJA DE DISCOS

Aluno1: Filipe das Chagas Pinheiro
   Mat: 2019018442

Aluno2: Rodrigo Soares Lima
   Mat: 2019018522
'''

print(cabecalho)

biblioteca = {}

table_data = [['Código', 'Album', 'Artista', 'Ano', 'Preço (R$)']]

layout_menu = [['Digite uma opção'], ['[1]Cadastrar Album'], ['[2]Listar Album(s)'], ['[3]Pesquisar'], ['[4]Excluir Item(s)'], ['[5]Alterar Item(s)'], ['[0]Sair']]
layout_data = AsciiTable(layout_menu)

menu_pesquisa = [['Pesquisar por:'], ['[1] Código'], ['[2] Album'], ['[3] Artista'], ['[4] Ano'], ['[5] Preço'], ['[6] Voltar']]
menu_data = AsciiTable(menu_pesquisa)

menu_altera = [['Alterar qual informação?'], ['[1] Album'], ['[2] Artista'], ['[3] Ano'], ['[4] Preço'], ['[5] Voltar']]
altera_data = AsciiTable(menu_altera)

while True:

    menu = int(input(layout_data.table + '\n'))

    if menu == 1:
        codigo = input("Insira um codigo:").upper()
        album = input("Insira o nome do album:").upper()
        artista = input("Insira o nome do artista:").upper()
        ano = int(input("Insira o ano de lançamento:"))
        preco = round(float(input("Insira o preço:")), 2)

        cadastro(biblioteca, codigo, album, artista, ano, preco)
        print('\nItem cadastrado com sucesso!\n')

    elif menu == 2:
        contador_preco = 0
        contador_item = 0

        for key in biblioteca:
            contador_item += 1
            contador_preco += biblioteca[key]['preco']
            nova_lista = list(biblioteca[key].values())
            nova_lista.insert(0, key)
            table_data.append(nova_lista)
        array_sigma = ['Total', '{} item(s)'.format(contador_item), '---------','---------', contador_preco, ]
        table_data.append(array_sigma)
        table = AsciiTable(table_data)
        print(table.table)
        table_data = [['Código', 'Album', 'Artista', 'Ano', 'Preço (R$)']]

    elif menu == 3:
        valor_pesquisa = int(input(menu_data.table + '\n'))

        if valor_pesquisa == 1:
            codigo_valor = input('Digite o codigo desejado: ').upper()

            for key in biblioteca:
                if key == codigo_valor:
                        nova_lista = list(biblioteca[key].values())
                        nova_lista.insert(0, key)
                        table_data.append(nova_lista)
                        table = AsciiTable(table_data)
            print(table.table)
            table_data = [['Código', 'Album', 'Artista', 'Ano', 'Preço']]

        elif valor_pesquisa == 2:
            album_valor = input('Digite o album desejado: ').upper()

            for key in biblioteca:
                if biblioteca[key]['album'] == album_valor:
                        nova_lista = list(biblioteca[key].values())
                        nova_lista.insert(0, key)
                        table_data.append(nova_lista)
                        table = AsciiTable(table_data)
            print(table.table)
            table_data = [['Código', 'Album', 'Artista', 'Ano', 'Preço']]

        elif valor_pesquisa == 3:
            artista_valor = input('Digite o artista desejado: ').upper()

            for key in biblioteca:
                if biblioteca[key]['artista'] == artista_valor:
                        nova_lista = list(biblioteca[key].values())
                        nova_lista.insert(0, key)
                        table_data.append(nova_lista)
                        table = AsciiTable(table_data)
            print(table.table)
            table_data = [['Código', 'Album', 'Artista', 'Ano', 'Preço']]

        elif valor_pesquisa == 4:
            ano_valor = int(input('Digite o ano desejado: '))

            for key in biblioteca:
                if biblioteca[key]['ano'] == ano_valor:
                    nova_lista = list(biblioteca[key].values())
                    nova_lista.insert(0, key)
                    table_data.append(nova_lista)
                    table = AsciiTable(table_data)
            print(table.table)
            table_data = [['Código', 'Album', 'Artista', 'Ano', 'Preço']]

        elif valor_pesquisa == 5:

            preco_valor = float(input('Digite o preco maximo do item desejado: '))

            for key in biblioteca:
                if biblioteca[key]['preco'] <= preco_valor:
                    nova_lista = list(biblioteca[key].values())
                    nova_lista.insert(0, key)
                    table_data.append(nova_lista)
                    table = AsciiTable(table_data)
            print(table.table)
            table_data = [['Código', 'Album', 'Artista', 'Ano', 'Preço']]

    elif menu == 4:
        deletar_codigo = input("Insira o codigo do item a ser excluido: ").upper()
        deletar(deletar_codigo, biblioteca)
        print('\nItem excluido com sucesso!\n')

    elif menu == 5:
        codigo_valor = input('Digite o codigo do item a ser alterado: ').upper()

        for key in biblioteca:
            if key == codigo_valor:
                opcao_alterar = int(input(altera_data.table + '\n'))

                if opcao_alterar == 1:
                    biblioteca[key]['album'] = input('Edite o nome do album: ').upper()
                    print('\nItem alterado!\n')

                elif opcao_alterar == 2:
                    biblioteca[key]['artista'] = input('Edite o nome do artista: ').upper()
                    print('\nItem alterado!\n')

                elif opcao_alterar == 3:
                    biblioteca[key]['ano'] = int(input('Edite o ano: '))
                    print('\nItem alterado!\n')

                elif opcao_alterar == 4:
                    biblioteca[key]['preco'] = float(input('Edite o preco: '))
                    print('\nItem alterado!\n')


    elif menu == 0:
        sair()
        break
