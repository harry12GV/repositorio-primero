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

    def eliminar_multiplos(self):
        while self.p is not None and self.p.valor % 2 == 0:
            self.p = self.p.siguiente
        
        actual = self.p
        while actual is not None and actual.siguiente is not None:
            if actual.siguiente.valor % 2 == 0:
                actual.siguiente = actual.siguiente.siguiente
            else:
                actual = actual.siguiente

lista1 = Lista()
lista1.agregar_final(12)
lista1.agregar_final(10)
lista1.agregar_final(13)
lista1.agregar_final(22)
lista1.agregar_final(32)
lista1.imprimir_lista()

lista1.eliminar_multiplos()
lista1.imprimir_lista()
