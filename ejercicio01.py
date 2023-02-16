class Cola:
    def _init_(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0,item)

    def avanzar(self):
        return self.items.pop()

    def tamano(self):
        return len(self.items)

    def imprimir(self):
        
        print("Lista de compras")
        print(self.items)
            
def agregarCompra():
    agregar = input("Añadir compra: ")
    c.agregar(agregar)

def eliminarCompra():
    print("Se quito:")
    print(c.avanzar())
    

#Programa Principal

c = Cola()
while True:
    print("Menú")
    print("[1]Añadir compra")
    print("[2]Quitar compra")
    print("[3]Imprimir compras")
    print("[0]salir")
    n = int(input("Ingrese opción: "))
    if n == 1:
        agregarCompra()
    elif n == 2:
        eliminarCompra()
    elif n ==3:
        c.imprimir()
    else:
        print("saliendo")
        break