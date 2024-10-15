from clase_nodo import Nodo
class Lista:
    
    def __init__(self):
        self.p = None

    def es_vacio(self):
        return self.p is None
    
    def agregar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.p is None:
            self.p = nuevo_nodo
        else:
            actual = self.p
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def agregar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.p is None:
            self.p = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.p
            self.p = nuevo_nodo

    def imprimir_lista(self):
        actual = self.p
        while actual is not None:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")
    
    def contar_nodos(self):
        actual = self.p
        contador = 0
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador
    
    def eliminar_inicio(self):
        if self.p is not None:
            self.p = self.p.siguiente

    def encontrar_mayor(self):
        if self.p is None:
            return None
        mayor = self.p.valor
        actual = self.p
        while actual is not None:
            if actual.valor > mayor:
                mayor = actual.valor
            actual = actual.siguiente
        return mayor

    def unir_y_ordenar(self, otra_lista):
        
        if self.p is None:
            self.p = otra_lista.p
        else:
            actual = self.p
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = otra_lista.p
        
    
        elementos = []
        actual = self.p
        while actual is not None:
            elementos.append(actual.valor)
            actual = actual.siguiente
        
            elementos.sort()
        
        self.p = None
        for elemento in elementos:
            self.agregar_final(elemento)


lista1 = Lista()
lista2 = Lista()

lista1.agregar_final('2')
lista1.agregar_final('0')
lista1.agregar_final('1')
lista2.agregar_final('4')
lista2.agregar_final('5')
lista2.agregar_final('8')
lista1.unir_y_ordenar(lista2)
lista1.imprimir_lista()
mayor_lista1 = lista1.encontrar_mayor()
mayor_lista2 = lista2.encontrar_mayor()


if mayor_lista1 > mayor_lista2:
    print("esta lista contiene el mayor caracter:", mayor_lista1)
else:
    print("esta list contiene el mayor carecter:", mayor_lista2)

