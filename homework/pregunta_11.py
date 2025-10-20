"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    diccionario = {}
    with open('files\input\data.csv') as archivo:
        for linea in archivo.readlines():
            l = linea.split()
            entrada = l[3].split(',')
            num = int(l[1])
            for dato in entrada:
                if dato not in diccionario:
                    diccionario[dato] = 0
                diccionario[dato] += num
    return dict(sorted(diccionario.items()))

        