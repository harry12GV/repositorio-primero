class Cola_Simple:
    def __init__(self, max_size):
        self.max = max_size
        self.cola = [None]*(self.max + 1)
        self.front = 0
        self.back = 0
    def es_vacia(self):
        return self.front == 0 and self.back ==0
    
    def es_llena(self):
        return self.back ==self.max
    
    def size(self):
        return self.back - self.front
    
    def enqueue(self, elemento):
        if not self.es_llena():
            self.back +=1
            self.cola[self.back]= elemento
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
            print("la cola esta:",self.cola[self.front + 1:self.back + 1])
      
Cola = Cola_Simple(4)
Cola.enqueue(20)
Cola.enqueue(30)
Cola.enqueue(9)
Cola.enqueue(2)
Cola.mostrar()
Cola.dequeue()
Cola.mostrar()


