"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    diccionario = {}
    rta = []
    with open('files\input\data.csv') as archivo:
        for linea in archivo.readlines():
            l = linea.split()
            entrada = l[4].split(',')
            for dato in entrada:
                i, _ = dato.split(':')
                if i not in diccionario:
                    diccionario[i] = 0
                diccionario[i] += 1
    return diccionario

