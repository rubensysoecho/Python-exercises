class Contrato:
    
    def __init__(self, numContrato, dni, nombre = "", apellidos = "", sbm = 0, irpf = 0):
        self.__numContrato = numContrato
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__sbm = sbm
        self.__irpf = irpf

    def getNumContrato(self):
        return self.__numContrato
    
    def setNumContrato(self, numContrato):
        self.__numContrato = numContrato
        
    def getDni(self):
        return self.__dni
    
    def setDni(self, dni):
        self.__dni = dni
        
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getApellidos(self):
        return self.__apellidos
    
    def setApellidos(self, apellidos):
        self.__apellidos = apellidos
        
    def getSbm(self):
        return self.__sbm
    
    def setSbm(self, sbm):
        self.__sbm = sbm
        
    def getIrpf(self):
        return self.__irpf
    
    def setIrpf(self, irpf):
        self.__irpf = irpf
        
    def salario_neto(self):
        return self.__sbm * self.__irpf
    
    def ver_datos(self):
        print("Nº contrato:", self.__numContrato)
        print("DNI:", self.__dni)
        print("Nombre:", self.__nombre)
        print("Apellidos:", self.__apellidos)
        print("Salario bruto mensual (SBM):", self.__sbm)
        print("IRPF:", self.__irpf)
    
class ContratoIndefinido(Contrato):
    
    def __init__(self, numContrato, dni, nombre, apellidos, sbm, irpf, pagas_prorrateadas):
        super().__init__(numContrato, dni, nombre, apellidos, sbm, irpf)
        self.__pagas_prorrateadas = pagas_prorrateadas
        
    def getPagasProrrateadas(self):
        return self.__pagas_prorrateadas
    
    def setPagasProrrateadas(self, pagas):
        self.__pagas_prorrateadas = pagas
    
    def ver_datos(self):
        super().ver_datos()
        print("Pagas Prorrateadas:", self.__pagas_prorrateadas)
    
class ContratoTemporal(Contrato):
    
    def __init__(self, numContrato, dni, nombre, apellidos, sbm, irpf, mesesDuracion):
        super().__init__(numContrato, dni, nombre, apellidos, sbm, irpf)
        self.__mesesDuracion = mesesDuracion
        
    def getMesesDuracion(self):
        return self.__mesesDuracion
    
    def setMesesDuracion(self, meses):
        self.__mesesDuracion = meses
    
    def ver_datos(self):
        super().ver_datos()
        print("Meses de duración:", self.__mesesDuracion)
    
class ContratoPracticas(Contrato):
    
    def __init__(self, numContrato, dni, nombre, apellidos, sbm, irpf, titulacionCursada, mesesDuracion):
        super().__init__(numContrato, dni, nombre, apellidos, sbm, irpf)
        self.__titulacionCursada = titulacionCursada
        self.__mesesDuracion = mesesDuracion
        
    def getTitulacionCursada(self):
        return self.__titulacionCursada

    def setTitulacionCursada(self, titulacion):
        self.__titulacionCursada = titulacion    
    
    def getMesesDuracion(self):
        return self.__mesesDuracion
    
    def setMesesDuracion(self, meses):
        self.__mesesDuracion = meses
        
    def ver_datos(self):
        super().ver_datos()
        print("Titulación cursada:", self.__titulacionCursada)
        print("Meses de duración:", self.__mesesDuracion)
        
contratoIndefinido = ContratoIndefinido(1, "12122323A", "Alfonso", "González", 1200, 0.65, True)
contratoTemporal = ContratoTemporal(2, "65654343R", "Javier", "Sampedro", 1000, 0.8, 12)
contratoPracticas = ContratoPracticas(3, "09099797T", "Gilberto", "Rodríguez", 2500, 0.6, "Desarrollo de aplicaciones multiplataforma", 5)

contratoIndefinido.ver_datos()
print()
contratoTemporal.ver_datos()
print()
contratoPracticas.ver_datos()