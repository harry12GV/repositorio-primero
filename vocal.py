def es_vocal(caracter):
    return caracter.lower()

def verificar_vocales(pila):
    vocales = []
    while pila:
        caracter = pila.pop()
        if es_vocal(caracter):
            vocales.append(caracter)
    return vocales


pila = ['a', 'b', 'c', 'e', 'i', 'o', 'u', 'x', 'y', 'z']
vocales_encontradas = verificar_vocales(pila)
print("estas son las vocales:", vocales_encontradas)
