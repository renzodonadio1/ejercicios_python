#formula = a[n] = a[n-1] * r
#a1 = 2
#r = -3

def termino(num1: int) -> int:
    if num1 == 1:
        return 2
    return termino(num1 - 1) * (-3)

#para mostrar la sucesion

def mostrar_sucesion(num1: int, i=1):
    if i > num1:
        return
    print(termino(i))
    mostrar_sucesion(num1, i + 1)

mostrar_sucesion(5)