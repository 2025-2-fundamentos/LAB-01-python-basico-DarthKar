"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    lista = {}
    rta = []
    with open(r'files\input\data.csv') as archivo:
        for linea in archivo.readlines():
            l = linea.split()
            if l[0] not in lista:
                lista[l[0]] = 1
            else:
                lista[l[0]] += 1
    for letra in lista:
        rta.append((letra, lista[letra]))
    return sorted(rta)

