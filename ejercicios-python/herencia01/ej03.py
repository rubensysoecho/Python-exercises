class Componente:
    
    def __init__(self, referencia, precio, marca):
        self.__referencia = referencia
        self.__precio = precio
        self.__marca = marca
    
    def getReferencia(self):
       return self.__referencia 
    
    def getPrecio(self):
       return self.__precio
   
    def getMarca(self):
       return self.__marca
   
    def setReferencia(self, referencia):
        self.__referencia = referencia
    
    def setPrecio(self, precio):
        self.__precio = precio
        
    def setMarca(self, marca):
        self.__marca = marca
        
    def precioDescuento(self, descuento):
        return self.__precio - (self.__precio * descuento)

    def ver_datos(self):
        print("Referencia ->", self.__referencia)
        print("Precio ->", self.__precio, "euros")
        print("Marca ->", self.__marca)
    
class DiscoDuro(Componente):
    
    def __init__(self, referencia, precio, marca, capacidadTB, tipoBus):
        super().__init__(referencia, precio, marca)
        self.__capacidadTB = capacidadTB
        self.__tipoBus = tipoBus
        
    def getCapacidadTB(self):
        return self.__capacidadTB
    
    def getTipoBus(self):
        return self.__tipoBus
    
    def setCapacidadTB(self, capacidad):
        self.__capacidadTB = capacidad
        
    def setTipoBus(self, tipoBus):
        self.__tipoBus = tipoBus
        
class TarjetaGrafica(Componente):
    
    def __init__(self, referencia, precio, marca, modelo, memoriaMB, tipoBus):
        super().__init__(referencia, precio, marca)
        self.__modelo = modelo
        self.__memoriaMB = memoriaMB
        self.__tipoBus = tipoBus
        
    def getModelo(self):
        return self.__modelo
    
    def getMemoriaMB(self):
        return self.__memoriaMB
    
    def getTipoBus(self):
        return self.__tipoBus
    
    def setModelo(self, modelo):
        self.__modelo = modelo
        
    def setMemoriaMB(self, memoriaMB):
        self.__memoriaMB = memoriaMB
        
    def setTipoBus(self, tipoBus):
        self.__tipoBus = tipoBus
        
    def conversorGB(self):
        return self.__memoriaMB / 1024
    
    def precioDescuento(self, descuento):
        return super().getPrecio()
    
class Pendrive(Componente):
    
    def __init__(self, referencia, precio, marca, capacidad):
        super().__init__(referencia, precio, marca)
        self.__capacidad = capacidad
        
    def getCapacidad(self):
        return self.__capacidad
    
    def setCapacidad(self, capacidad):
        self.__capacidad = capacidad
        
    def ver_datos(self):
        super().ver_datos()
        print("Capacidad ->", self.__capacidad, "Gb")
        
    
discoDuro = DiscoDuro("HD1050", 118.77, "Western Digital", 2, "SATA3")
tarjetaGrafica = TarjetaGrafica("TG0004", 131.28, "ASUS", "GTX550", 1024, "PCI Express")

print("Precio Disco Duro ->", discoDuro.getPrecio(), "euros")
print("Precio Tarjeta Grafica ->", tarjetaGrafica.getPrecio(), "euros")

print()

print("Precio Disco Duro (+descuento) ->", discoDuro.precioDescuento(0.15), "euros")
print("Precio Tarjeta Grafica (+descuento) ->", tarjetaGrafica.precioDescuento(0.15), "euros")

print("Memoria de la Gráfica (Gb) ->", tarjetaGrafica.conversorGB(), "Gb")

print()

pendrive = Pendrive("USB1001", 18, "SanDisk", 16)
print("Precio Pendrive (+descuento) ->", pendrive.precioDescuento(0.1))

print()

pendrive.setPrecio(20)
pendrive.setReferencia("USB1002")

pendrive.ver_datos()

