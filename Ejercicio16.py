#formula = a[n] = a[n-1] * r
#a1 = 2
#r = -3

def termino(num1: int) -> int:
    if num1 == 0:
        return 2
    return termino(num1 - 1) * (-3)

#para mostrar la sucesion

def mostrar_sucesion(num1: int)