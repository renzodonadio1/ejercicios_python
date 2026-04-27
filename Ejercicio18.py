def recorrer_matriz(matrizA, i=0, j=0):
    if i >= len(matrizA):
        return
    
    if j >= len(matrizA[i]):
        recorrer_matriz(matrizA, i + 1, 0)
        return
     
print(matrizA[i][j])
recorrer_matriz(matrizA, i, j + 1)