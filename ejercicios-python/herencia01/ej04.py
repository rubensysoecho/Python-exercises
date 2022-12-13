class FacturaAgua:
    
    def __init__(self, numFactura, fecha, dniCliente, precioMetroCuadrado, metrosCubicosConsumidos, importeSaneamiento, importeResiduales):
        self.__numFactura = numFactura
        self.__fecha = fecha
        self.__dniCliente = dniCliente
        self.__precioMetroCuadrado = precioMetroCuadrado
        self.__metrosCubicosConsumidos = metrosCubicosConsumidos
        self.__importeSaneamiento = importeSaneamiento
        self.__importeResiduales = importeResiduales
        
    def getNumFactura(self):
        return self.__numFactura
    
    def getFecha(self):
        return self.__fecha
    
    def getDniCliente(self):
        return self.__dniCliente
    
    def getPrecioMetroCuadrado(self):
        return self.__precioMetroCuadrado
    
    def getMetrosCubicosConsumidos(self):
        return self.__metrosCubicosConsumidos
    
    def getImporteSaneamiento(self):
        return self.__importeSaneamiento
    
    def getImporteResiduales(self):
        return self.__importeResiduales
    
    def setNumFactura(self, numFactura):
        self.__numFactura = numFactura
    
    def setFecha(self, fecha):
        self.__fecha = fecha
    
    def setDniCliente(self, dniCliente):
        self.__dniCliente = dniCliente
    
    def setPrecioMetroCuadrado(self, precioMetroCuadrad):
        self.__precioMetroCuadrado = precioMetroCuadrad
    
    def setMetrosCubicosConsumidos(self, metrosCubicosConsumidos):
        self.__metrosCubicosConsumidos = metrosCubicosConsumidos
        
    def setImporteSaneamiento(self, importeSaneamiento):
        self.__importeSaneamiento = importeSaneamiento
        
    def setImporteResiduales(self, importeResiduales):
        self.__importeResiduales = importeResiduales
        
    def importePorConsumo(self):
        return self.__metrosCubicosConsumidos * self.__precioMetroCuadrado
    
    def totalFactura(self):
        return self.importePorConsumo() + self.__importeSaneamiento + self.__importeResiduales
    
class FacturaFamiliaNumerosaA(FacturaAgua):
    
    def __init__(self, numFactura, fecha, dniCliente, precioMetroCuadrado, metrosCubicosConsumidos, importeSaneamiento, importeResiduales):
        super().__init__(numFactura, fecha, dniCliente, precioMetroCuadrado, metrosCubicosConsumidos, importeSaneamiento * 0.8, importeResiduales * 0.8)
        
class FacturaFamiliaNumerosaB(FacturaAgua):
    
    def __init__(self, numFactura, fecha, dniCliente, precioMetroCuadrado, metrosCubicosConsumidos, importeSaneamiento, importeResiduales):
        super().__init__(numFactura, fecha, dniCliente, precioMetroCuadrado, metrosCubicosConsumidos, importeSaneamiento * 0.25, importeResiduales * 0.5)
        
facturaNormal = FacturaAgua(1, "20/02/2010", "12341234A", 50, 100, 100, 200)
facturaNumerosaA = FacturaFamiliaNumerosaA(2, "20/02/2010", "12341234A", 50, 100, 100, 200)
facturaNumerosaB = FacturaFamiliaNumerosaB(3, "20/02/2010", "12341234A", 50, 100, 100, 200)

print("Normal ->", facturaNormal.totalFactura(), "euros")
print("Familia numerosa A ->", facturaNumerosaA.totalFactura(), "euros")
print("Familia numerosa B ->", facturaNumerosaB.totalFactura(), "euros")