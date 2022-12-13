import datetime as dt

class Jugador:
    
    def __init__(self, nombre, apellidos, dorsal, mediaPuntos):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__dorsal = dorsal
        self.__mediaPuntos = mediaPuntos
        
    def getNombre(self):
        return self.__nombre
    
    def getApellidos(self):
        return self.__apellidos
    
    def getDorsal(self):
        return self.__dorsal
    
    def getMediaPuntos(self):
        return self.__mediaPuntos
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def setApellidos(self, apellidos):
        self.__apellidos = apellidos
        
    def setDorsal(self, dorsal):
        if dorsal < 1 or dorsal > 100:
            print("ERROR. El dorsal debe ser un numero entre 1 y 100.")
        else:
            self.__dorsal = dorsal
        
    def setMediaPuntos(self, mediaPuntos):
        if mediaPuntos < 0:
            print("ERROR. La media de puntos debe ser positiva.")
        else:
            self.__mediaPuntos = mediaPuntos
            
    def ver_datos(self):
        print("Nombre:", self.__nombre)
        print("Apellidos:", self.__apellidos)
        print("Dorsal:", self.__dorsal)
        print("Media de puntos/partido:", self.__mediaPuntos)
        print()
        
class EquipoBaloncesto:
    
    def __init__(self, nombre, fechaFundacion = "", jugadores = "Ninguno"):
        self.__nombre = nombre
        self.__fechaFundacion = fechaFundacion
        self.__jugadores = jugadores
        
    def getNombre(self):
        return self.__nombre
    
    def getFechaFundacion(self):
        return self.__fechaFundacion
    
    def getJugadores(self):
        return self.__jugadores
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def setFechaFundacion(self, fechaFundacion):
        self.__fechaFundacion = fechaFundacion
        if fechaFundacion > dt.datetime.today():
            print("ERROR. La fecha de fundación no puede ser posterior a la fecha actual.")
        else:
            self.__fechaFundacion = fechaFundacion
    
    def setJugadores(self, jugadores):
        self.__jugadores = jugadores
        
    def maximo_anotador(self):
        maxAnotador = self.__jugadores[0]
        for i in range(1, 5):
            if self.__jugadores[i].getMediaPuntos() > maxAnotador.getMediaPuntos():
                maxAnotador = self.__jugadores[i]
        return maxAnotador
        
    def ver_datos(self):
        print("EQUIPO")
        print("------")
        print("Nombre:", self.__nombre)
        print("Fecha de fundación:", self.__fechaFundacion)
        print("------")
        print("JUGADORES")
        print("------")
        for i in range(0, 5):
            self.__jugadores[i].ver_datos()
        print("------")
        print("MÁXIMO ANOTADOR")
        print("------")
        self.maximo_anotador().ver_datos()
        
            
            
jugador1 = Jugador("Alfonso", "Gómez", 1, 2.5)
jugador2 = Jugador("Gabriel", "Aldán", 2, 7.1)
jugador3 = Jugador("Victor", "Rodriguez", 3, 10)
jugador4 = Jugador("Joel", "Hidalgo", 4, 15)
jugador5 = Jugador("León", "Romero", 5, 1)
    
jugadores = [jugador1, jugador2, jugador3, jugador4, jugador5]

fechaFundacion = dt.datetime(1964, 2, 10)
equipo = EquipoBaloncesto("Caceres B.C", fechaFundacion, jugadores)

equipo.ver_datos()