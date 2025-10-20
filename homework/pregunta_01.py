"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import os

def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214
    """
    dir_actual = os.path.dirname(__file__)
    ruta = os.path.join(dir_actual, 'files', 'input', 'data.csv')

    suma = 0
    with open(ruta) as archivo:
        for linea in archivo:
            suma += int(linea.split()[1])
    return suma
