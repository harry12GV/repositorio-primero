class pila():
    def __init__(self): 
        self.datos = []
        
    def push(self, dato):
        self.datos.append(dato)
        print(f'el elemento {dato} ha sido apilado')
        
    def pop(self):
        if not self.datos.vacia:
            self.datos.pop()
            print('el items  esta siendo desapilado')
        else:
            print('la pila esta vacia')
        return ()
        
    def vacia(self):
        if len(self.dato)==0:
         return()
        
pila1 = pila()
pila1.push('henry')
pila1.push('carlos')

elemento = pila1.pop()
print(f'el elemento desapilado:{elemento}')
pila1.imprimir()















