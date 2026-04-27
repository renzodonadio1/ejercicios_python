lista = [1, 2, 3, 4, 5]

def vector_inverso(vector, i):
    if i < 0:
        return
    print(vector[i])
    vector_inverso(vector, i - 1)

print(vector_inverso(lista, len(lista)))