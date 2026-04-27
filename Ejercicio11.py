def invertir_numero(num1:int, numero_invertido=0) -> int:
    if num1 == 0:
        return numero_invertido
    return invertir_numero(num1 // 10, numero_invertido=numero_invertido * 10 + num1 % 10)