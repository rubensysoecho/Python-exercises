class Vehiculo:
    
    def __init__(self, marca, modelo, color, num_ruedas, precio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.num_ruedas = num_ruedas
        self.precio = precio
         
    def precio_IVA(self):
        return self.precio * 1.21

    def verDatos(self):
        print(f"{self.marca}, {self.modelo}, {self.color}, {self.num_ruedas}, {self.precio}, {self.precio_IVA()}")


vehiculo1 = Vehiculo("Seat", "Ibiza", "Rojo", 4, 11500)
vehiculo2 = Vehiculo("Yamaha", "MT-03", "Negro", 2, 6000)

vehiculo1.verDatos()
vehiculo2.verDatos()