def busqueda_centinela(lista, valor, i=0):
    if lista[i] == valor:
        return i
    return busqueda_centinela(lista, valor, i + 1)