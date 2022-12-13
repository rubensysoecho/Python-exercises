class Pendrive:
    
    iva = 0.18
    
    def __init__(self, marca, modelo, capacidad, precio):
        self.__marca = marca
        self.__modelo = modelo
        self.capacidad = capacidad
        self.precio = precio
    
    def precioIVA(self, ):
        return self.precio + (self.precio * self.iva)

marca = input("Marca: ")
modelo = input("Modelo: ")
capacidad = int(input("Capacidad: "))
precio = float(input("Precio: "))

pendrive = Pendrive(marca, modelo, capacidad, precio)
print(f"Precio con IVA --> {pendrive.precioIVA()}")