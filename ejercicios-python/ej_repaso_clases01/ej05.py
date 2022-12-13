class Articulo:
    
    __IVA = 0.18
    
    def __init__(self, referencia, precio):
        self.__referencia = referencia
        if precio < 0:
            print("ERROR. El precio debe ser positivo.")
            self.__precio = ""
        else:
            self.__precio = precio
        
    def getReferencia(self):
        return self.__referencia
    
    def getPrecio(self):
        return self.__precio
    
    def setReferencia(self, ref):
        self.__referencia = ref
        
    def setPrecio(self, precio):
        if precio < 0:
            print("ERROR. El precio debe ser positivo.")
        else:
            self.__precio = precio
        
    def precioFinal(self, descuento = ""):
        if descuento == "":
            return self.__precio * (1 + self.__IVA)
        else:
            if descuento < 0 or descuento > 1:
                print("ERROR. El descuento debe oscilar entre 0 y 1.")
            else:
                return self.__precio * (1 - descuento) * (1 + self.__IVA)
            
        
articuloMal1 = Articulo("MAL-1", -300)
articuloMal2 = Articulo("MAL-2", -1)

articulo = Articulo("X1002", 100)
print("Precio Final ->", articulo.precioFinal(), "euros")
print("Precio Final ->", articulo.precioFinal(0.5), "euros")