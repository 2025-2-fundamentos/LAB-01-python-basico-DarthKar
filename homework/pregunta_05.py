"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    lista = {}
    rta = []
    with open('files\input\data.csv') as archivo:
        for linea in archivo.readlines():
            l = linea.split()
            if l[0] not in lista:
               lista[l[0]] = []
            lista[l[0]].append(int(l[1]))
    for letra in lista:
        rta.append((letra, max(lista[letra]), min(lista[letra])))


    return sorted(rta)


            

        