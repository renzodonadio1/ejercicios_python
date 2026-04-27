lista = [1, 2, 3, 4, 5]

def busqueda_centinela(lista, valor, i=0):
    if lista[i] == valor:
        return i
    return busqueda_centinela(lista, valor, i + 1)

def buscar(lista, valor):
    lista.append(valor)

    pos = busqueda_centinela(lista, valor)

    lista.pop()

    if pos < len(lista):
        return f"El valor {valor} se encuentra en la posición {pos}"
    else:
        return f"El valor {valor} no se encuentra en la lista"

print(buscar(lista, 3))
print(buscar(lista, 10))