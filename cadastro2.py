def cadastro(biblioteca, codigo, album, artista, ano, preco):

    biblioteca[codigo] = {
        'album': album,
        'artista': artista,
        'ano': ano,
        'preco': preco
    }

def sair():
    print('Atividade encerrada')

def deletar(key, dicionario):
        del dicionario[key]

#Terminaltables
