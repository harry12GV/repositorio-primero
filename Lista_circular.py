from clase_nodo import Nodo

class ListaCircular:
    def __init__(self):
        self.p = None

    def es_vacio(self):
        return self.p is None
    
    def agregar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.p is None:
            self.p = nuevo_nodo
            self.p.siguiente = self.p
        else:
            actual = self.p
            while actual.siguiente != self.p:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.p
            
    def agregar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.p is None:
            self.p = nuevo_nodo
            self.p.siguiente = self.p
        else:
            nuevo_nodo.siguiente = self.p
            actual = self.p
            while actual.siguiente != self.p:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            self.p = nuevo_nodo
            
    def imprimir_lista(self):
        if self.p is None:
            print("La lista esta vacia")
            return
        actual = self.p
        while True:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
            if actual == self.p:
                break
        print()
    def mostrar_lista(self):
        if self.es_vacio():
            print("La lista esta vacia")
           
        else:
            actual=self.p
            bandera=True
            while bandera:
              print(actual.valor, end=" -> ")
              actual = actual.siguiente
              if actual == self.p:
                bandera=False
        print("(de nuevo al inicio)")
            
    
    def eliminar_inicio(self):
        if self.p is not None:
            if self.p.siguiente == self.p:
                self.p = None
            else:
                actual = self.p
                while actual.siguiente != self.p:
                    actual = actual.siguiente
                actual.siguiente = self.p.siguiente
                self.p = self.p.siguiente
                
    def eliminar_final(self):
        if self.p is not None:
            if self.p.siguiente == self.p:
                self.p = None
            else:
                actual = self.p
                while actual.siguiente.siguiente != self.p:
                    actual = actual.siguiente
                actual.siguiente = self.p

lista1 = ListaCircular()
lista1.agregar_final("pedro")
lista1.agregar_final("ivan")
lista1.agregar_final("zambrana")
lista1.agregar_final("muriel")
lista1.agregar_inicio("huaytari")
lista1.imprimir_lista()  

lista1.mostrar_lista()
lista1.eliminar_final()
lista1.imprimir_lista()

   
        

            