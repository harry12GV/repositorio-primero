class Cola_Simple:
    def __init__(self, max_size):
        self.max = max_size
        self.cola = [None]*(self.max + 1)
        self.front = 0
        self.back = 0

    def es_vacia(self):
        return self.front == 0 and self.back == 0
    
    def es_llena(self):
        return self.back == self.max
    
    def size(self):
        return self.back - self.front
    
    def enqueue(self, elemento):
        if not self.es_llena():
            self.back += 1
            self.cola[self.back] = elemento
        else:
            print("la cola esta llena")
    
    def dequeue(self):
        elemento = None
        if not self.es_vacia():
            self.front += 1
            elemento = self.cola[self.front]
            if self.front == self.back:
                self.front = 0
                self.back = 0
        else:
            print("la cola esta vacia")
        return elemento
    
    def mostrar(self):
        if self.es_vacia():
            print("cola vacia")
        else:
            print("la cola esta:", self.cola[self.front + 1:self.back + 1])
    
    def numero_mayor(self):
        if self.es_vacia():
            return None
        return max(self.cola[self.front + 1:self.back + 1])
    
    def mostrar_pares(self):
        if self.es_vacia():
            print("cola vacia")
        else:
            pares = [x for x in self.cola[self.front + 1:self.back + 1] if x is not None and x % 2 == 0]
            print("numeros pares en la cola:", pares)
   
# Ejemplo de uso
Cola = Cola_Simple(4)
for _ in range(4):
    elemento = int(input("ingrese datos de la cola: "))
    Cola.enqueue(elemento)

Cola.mostrar()
print("numero mayor en la cola:" , Cola.numero_mayor())

Cola.mostrar_pares()

Cola.dequeue()
Cola.mostrar()
