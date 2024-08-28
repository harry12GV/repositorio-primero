def ordenar_pila_descendente(pila):
    # Ordenamos la pila usando sorted() con reverse=True
    pila_ordenada = sorted(pila, reverse=True)
    return pila_ordenada

# Ejemplo de uso
pila = ['a', 'd', 'c', 'b', 'e']
pila_ordenada = ordenar_pila_descendente(pila)

print("Pila ordenada de forma descendente:", pila_ordenada)
