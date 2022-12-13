import datetime as dt

class Autor:
    
    def __init__(self, nombre, apellidos, anhoNacimiento = 0, pais = ""):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__anhoNacimiento = anhoNacimiento
        self.__pais = pais
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getApellidos(self):
        return self.__apellidos

    def setApellidos(self, apellidos):
        self.__apellidos = apellidos
        
    def getAnhoNacimiento(self):
        return self.__anhoNacimiento
    
    def setAnhoNacimiento(self, anho):
        if anho >= dt.date.today().year:
            print("ERROR. El año introducido es mayor al actual.")
        else:
            self.__anhoNacimiento = anho
        
    def getPais(self):
        return self.__pais
    
    def setPais(self, pais):
        self.__pais = pais
        
    def edad(self):
        return dt.date.today().year - self.__anhoNacimiento
        
    def ver_datos(self):
        print("Nombre:", self.__nombre)
        print("Apellidos:", self.__apellidos)
        print("Año de nacimiento:", self.__anhoNacimiento)
        print("País:", self.__pais)
        
class Libro:
    
    def __init__(self, autor, isbn, titulo, numPaginas = 0):
        self.__autor = autor
        self.__isbn = isbn
        self.__titulo = titulo
        self.__numPaginas = numPaginas
        
    def getAutor(self):
        return self.__autor.getNombre()
    
    def setAutor(self, autor):
        self.__autor = autor
        
    def getISBN(self):
        return self.__isbn
    
    def setISBN(self, isbn):
        self.__isbn = isbn
        
    def getTitulo(self):
        return self.__titulo
    
    def setTitulo(self, titulo):
        self.__titulo = titulo
        
    def getNumPaginas(self):
        return self.__numPaginas

    def setNumPaginas(self, numPaginas):
        if numPaginas < 0:
            print("ERROR. El numero de paginas debe ser positivo.")
        else:
            self.__numPaginas = numPaginas
            
    def ver_datos(self):
        print("Autor:")
        self.__autor.ver_datos()
        print("ISBN:", self.__isbn)
        print("Titulo:", self.__titulo)
        print("Nº paginas:", self.__numPaginas)
        
autor = Autor("Carlos", "Ruiz Zafón", 1964, "España")
libro = Libro(autor, "9788408105824", "El prisionero del Cielo", 245)

autor.setAnhoNacimiento(2022)
libro.setNumPaginas(-100)

libro.ver_datos()