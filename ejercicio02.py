class Pila:
    def _init_(self,size):
        self.lista = []
        self.tope = 0
        self.size = size
    
    def empty(self):
        if self.tope == 0:
            return True
        else:
            return False
        
    def push(self,dato):
        if self.tope < self.size:
            self.lista += [dato]
            self.tope += 1
        else:
            num = int(input("Cantidad de tareas agregar"))
            self.size += num
            if self.tope < self.size:
                self.lista += [dato]
                self.tope += 1           
    
    def pop(self):
        if self.empty():
            print("Trea Vacia")
        else:
            self.tope -= 1
            self.lista = [self.lista[x] for x in range(self.tope)]

    def show(self):
        i = self.tope - 1
        while i >-1:
            print(f'[{i}] >> {self.lista[i]}')
            i -= 1
    
    def lifoShow(self):
        return self.lista[-1]
    
try:
    if _name_ == "_main_":
        opcion = 0
        size = int(input("Cantidad elementos "))
        pila = Pila(size)
        while opcion != 6:
            print('PILAS: \n 1. Pila vacía?\n 2. Mostrar Tareas\n 3. Agregar Tarea\n 4. Eliminar Tarea\n 5. Mostrar última Tarea realizada\n 6.Salir')
            opcion = int(input('Ingrese opcion '))
            if opcion == 1:
                print("Si" if pila.empty() else "No")
            elif opcion == 2:
                pila.show()
            elif opcion == 3:
                dato = str(input("Ingrese un dato "))
                pila.push(dato)
            elif opcion == 4:
                pila.pop()
            elif opcion == 5:
                pila.lifoShow()
            elif opcion == 6:
                print("FIN")
            else:
                print("Ingrese un dato correcto")

except Exception as e:
    print(e)