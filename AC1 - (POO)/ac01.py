
'''
Implemente a função 'posicoes' que recebe como argumentos de entrada uma
tupla e um item, e retorna uma lista contendo todos os índices em que o
item aparece na tupla.
Caso o item nao exista na tupla, deve retornar uma lista vazia.
'''


def posicoes(tupla, item):
    teste = []
    for index, val in enumerate(tupla):

        if val == item:
            teste.append(index)

    return teste


'''
Implemente a função 'remover_itens_repetidos' que recebe como argumento
de entrada uma lista e remove todos os itens repetidos dessa lista. A função
deve retornar uma nova lista sem itens repetidos e ordenada de forma crescente.
'''


def remover_itens_repetidos(lista):
    ordenando = sorted(lista)
    remover_duplicatas = list(set(lista))

    return remover_duplicatas


'''
Considere um dicionario onde a chave é o nome de um aluno e o valor uma lista
de notas. Implemente a função 'media_notas' que recebe como argumento de
entrada o dicionário e retorna outro dicionário contendo os nomes e as médias
aritméticas de cada aluno.
'''


def media_notas(alunos):
    new_dic = {}
    for aluno in alunos:
        media = 0
        for notas in alunos[aluno]:
            media += notas
        media = media / len(alunos[aluno])
        new_dic[aluno] = media

    return new_dic


'''
Considere um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Implemente a função 'excluir_menor_nota' que recebe como argumentos
de entrada o dicionário e o nome de um aluno. A função deve excluir a menor
nota do aluno informado e retornar o dicionário com as alterações realizadas.
Se aluno não estiver no dicionário, deve retornar o dicionário sem alterações.
'''


def excluir_menor_nota(alunos, nome):

    if nome in alunos:
        notas = alunos[nome]
        menor = min(notas)
        notas = notas.pop(notas.index(menor))
    return alunos
    


'''
Implemente a função 'caracter_mais_frequente' que recebe como argumento de
entrada uma string e retorna o caracter que aparece com mais frequência na
string. Procure utilizar um dicionário para facilitar a implementação.
'''


def caracter_mais_frequente(texto):
    dicionario = {}
    for index, letras in enumerate(texto):
        cont = texto.count(letras)
        dicionario[letras] = cont

    keys = list(dicionario.keys())
    values = list(dicionario.values())
    max_val = max(dicionario.values())
    n = values.index(max_val)
    # indexOf(values, max_val)

    return keys[n]
