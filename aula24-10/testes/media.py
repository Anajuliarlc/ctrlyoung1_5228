def media(notas):
    """Calcula a média de uma lista de notas.

    :param valores: lista de notas (int ou float)
    :return: media das notas
    """
    if not notas:
        raise ValueError("A lista de valores não pode estar vazia.")
    soma = sum(notas)
    tamanho_lista = len(notas)
    media = round(soma/tamanho_lista, 2)

    return media

"""notas_young = [10.5, 8.6, 7, 5, 8, 9]
print(media(notas_young))"""