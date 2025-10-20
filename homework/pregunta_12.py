"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    di = {}
    with open(r'files\input\data.csv') as archivo:
        for linea in archivo.readlines():
            l = linea.split()
            letra = l[0]
            if letra not in di:
                di[letra] = 0
            entrada = l[4].split(',')
            for _ in entrada:
                clave, valor = _.split(':')
                di[letra]+=int(valor)
            
    return dict(sorted(di.items()))
