import datetime as dt

class Artista():
    
    def __init__(self, nombre, pais, anhoNacimiento):
        self.__nombre = nombre
        self.__pais = pais
        self.__anhoNacimiento = anhoNacimiento
        
    def getNombre(self):
        return self.__nombre

    def getPais(self):
        return self.__pais
    
    def getAnhoNacimiento(self):
        return self.__anhoNacimiento

    def edad(self):
        return dt.date.today().year - self.__anhoNacimiento
    
    def ver_datos(self):
        print("Nombre ->", self.__nombre)
        print("País ->", self.__pais)
        print("Año de nacimiento ->", self.__anhoNacimiento)
        print("Edad ->", self.edad())
        
class Disco:
    
    def __init__(self, titulo, artista, anhoLanzamiento = "/", numCanciones = "/"):
        self.__titulo = titulo
        self.__artista = artista
        self.__anhoLanzamiento = anhoLanzamiento
        self.__numCanciones = numCanciones
        
    def getTitulo(self):
        return self.__titulo
    
    def getArtista(self):
        return self.__artista.ver_datos()
    
    def getAnhoLanzamiento(self):
        return self.__anhoLanzamiento
    
    def getNumCanciones(self):
        return self.__numCanciones
    
    def setTitulo(self, titulo):
        self.__titulo = titulo
    
    def setArtista(self, artista):
        self.__artista = artista
        
    def setAnhoLanzamiento(self, anho):
        self.__anhoLanzamiento = anho
    
    def setNumCanciones(self, numCanciones):
        self.__numCanciones = numCanciones
        
    def antiguedad(self):
        return dt.date.today().year - self.__anhoLanzamiento
    
    def ver_datos(self):
        print("Titulo ->", self.__titulo)
        print("Artista ->", self.__artista.getNombre())
        print("Año de lanzamiento ->", self.__anhoLanzamiento)
        print("Nº de canciones ->", self.__numCanciones)
        
artista1 = Artista("Shakira", "Colombia", 1977)

disco = Disco("Sale el sol", artista1, 2009, 15)
disco.ver_datos()