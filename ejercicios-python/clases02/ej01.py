class Reloj:
    
    def __init__(self, marca, modelo, precio, stock, esDigital):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.stock = stock
        self.esDigital = esDigital
    
    def verDatos(self):
        print(f"{self.marca}, {self.modelo}, {self.precio} euros, {self.stock} unidades, {self.esDigital}")
        
reloj1 = Reloj("Casio", "X-300", 100, 10, "Si")
reloj2 = Reloj("Rolex", "J-5000", 400, 5, "No")

reloj1.verDatos()
reloj2.verDatos()

print("Suma de los precios:", reloj1.precio + reloj2.precio, "euros")