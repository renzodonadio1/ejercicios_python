def suma_digitos(num1:int) -> int:
    num1 = abs(num1) #abs = valor absoluto de un numero, para que funcione con numeros negativos
    if num1 < 10:
        return num1
    else:
        return (num1 % 10) + suma_digitos(num1 // 10)
    
print(suma_digitos(1234))
print(suma_digitos(-55))
print(suma_digitos(000))