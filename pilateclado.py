def llenar_teclado():
    Pila= Pila()
    print("Introduce elementos para la pila (escribe 'fin' para terminar):")
    while True:
        elemento = input("Elemento: ")
        if elemento.lower() == 'fin':
            break
        Pila.push(elemento)
    return Pila

# Ejemplo de uso
Pila = llenar_teclado()
print("Elementos en la pila:")
Pila.mostrar()
