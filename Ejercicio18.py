matrizA = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def recorrer_matriz(matrizA, i=0, j=0):
    if i >= len(matrizA):
        return
    
    if j >= len(matrizA[i]):
        print() #salto de linea
        recorrer_matriz(matrizA, i + 1, 0)
        return
     
    print(matrizA[i][j], end=' ')
    recorrer_matriz(matrizA, i, j + 1)

recorrer_matriz(matrizA)