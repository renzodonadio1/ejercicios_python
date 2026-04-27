def Fibonacci(n):
    if n < 0:
        return "el numero debe ser mayor o igual a  0" 
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)
    
print("valor de Fibonacci es:", Fibonacci(10))
