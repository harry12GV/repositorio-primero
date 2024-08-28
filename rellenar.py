def NUMEROS_pares_impares(pila):
    Pares = []
    Impares = []
    
    while pila:
        numero = pila.pop()
        if numero % 2 == 0:
            Pares.append(numero)
        else:
            Impares.append(numero)
    
    return Pares, Impares

# Ejemplo de uso
pila = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,["harry"]]
Pares, Impares = NUMEROS_pares_impares(pila)

print("Pila A:", Pares)
print("Pila B:", Impares)
