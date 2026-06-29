# forma: log_base(num) = log_base(num7base)

def logaritmo_entero(num:int, base:int) -> int:
    if num < base:
        return 0
    else:
        return 1 + logaritmo_entero(num // base,base)
    
print(logaritmo_entero(16,2))
print(logaritmo_entero(8,2))