def funcion(num1: int) -> float:
    if num1 == 1:
        return 1
    return num1 + 1 / funcion(num1 - 1)