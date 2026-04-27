def contar_digitos(num1:int) -> int:
    if num1 < 10:
        return 1
    else:
        return 1 + contar_digitos(num1 // 10)