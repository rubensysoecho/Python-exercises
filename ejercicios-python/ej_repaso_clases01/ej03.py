class Pelicula:
    
    def __init__(self, titulo, productora, director = "", duracion = "", puntuacion = ""):
        self.__titulo = titulo
        self.__productora = productora
        self.__director = director
        self.__duracion = duracion
        self.__puntuacion = puntuacion
        
    def getTitulo(self):
        return self.__titulo
    
    def getProductora(self):
        return self.__productora
    
    def getDirector(self):
        return self.__director
    
    def getDuracion(self):
        return self.__duracion
    
    def getPuntuacion(self):
        return self.__puntuacion
    
    def setTitulo(self, titulo):
        self.__titulo = titulo
        
    def setProductora(self, productora):
        self.__productora = productora
        
    def setDirector(self, director):
        self.__director = director
        
    def setDuracion(self, duracion):
        self.__duracion = duracion
        
    def setPuntuacion(self, puntuacion):
        if puntuacion < 0 or puntuacion > 10:
            print("La puntuacion debe oscilar entre 0 y 10")
        else:
            self.__puntuacion = puntuacion
        
    def ver_datos(self):
        print("PELICULA")
        print("--------")
        print("Titulo ->", self.__titulo)
        if self.__director == "":
            print("Director -> /")
        else:
            print("Director ->", self.__director)
        if self.__duracion == "":
            print("Duracion -> /")
        else:
            print("Duracion ->", self.__duracion, "minutos")
        if self.__puntuacion == "":
            print("Puntuacion -> /")
        else:
            print("Puntuacion ->", self.__puntuacion,"/ 10")
        print("--------")
        print("PRODUCTORA")
        print("--------")
        self.__productora.ver_datos()
        print("--------")

class Productora:
    
    def __init__(self, nombre, web):
        self.__nombre = nombre
        self.__web = web
        
    def getNombre(self):
        return self.__nombre

    def getWeb(self):
        return self.__web
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def setWeb(self, web):
        self.__web = web
        
    def ver_datos(self):
        print("Nombre ->", self.__nombre)
        print("Página Web ->", self.__web)


productora1 = Productora("Dreamworks Pictures", "http://www.dreamworksstudios.com/")
productora2 = Productora("Warner Bros. Pictures", "http://www.warnerbros.com/") 

pelicula1 = Pelicula("War Horse", productora1)
pelicula2 = Pelicula("Gran Torino", productora2, "Clint Eastwood", 119)

pelicula1.ver_datos()
pelicula2.ver_datos()

pelicula1.setDirector("Steven Spielberg")
pelicula1.setDuracion(146)
pelicula1.ver_datos()