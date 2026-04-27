lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def busqueda_BBIN(lista, valor, inicio, fin):
    if inicio > fin:
        return -1
    
    medio = (inicio + fin) // 2

    if lista[medio] == valor:
        return medio
    elif valor < lista[medio]:
        return busqueda_BBIN(lista, valor, inicio, medio - 1)
    else:
        return busqueda_BBIN(lista, valor, medio + 1, fin)
    
#

def buscar(lista, valor):
    pos = busqueda_BBIN(lista, valor, 0, len(lista) - 1)

    if pos != -1:
        return f"El valor {valor} se encuentra en la posición {pos}"
    else:
        return f"El valor {valor} no se encuentra en la lista"
    
print(buscar(lista, 3))
print(buscar(lista, 8))
print(buscar(lista, 21))
