"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214

    """
    suma = 0
    with open('https://github.com/2025-2-fundamentos/LAB-01-python-basico-DarthKar/blob/4f046d2c0e1789f28f56f720802a8ec2edfa75f7/files/input/data.csv') as archivo:
        for linea in archivo.readlines():
            suma+=int(linea.split()[1])
    return suma

