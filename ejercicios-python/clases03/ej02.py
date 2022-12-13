class Punto:
    
    __nombre = ""
    
    def __init__(self, x, y, nombre = ""):
        self.__x = x
        self.__y = y
        self.__nombre = nombre
    
    def asignar_nombre(self, nuevoNombre):
        self.__nombre = nuevoNombre
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getNombre(self):
        return self
    
    def desplaza_x(self, num):
        self.__x += num
    
    def desplaza_y(self, num):
        self.__y += num
        
    def ver_punto(self):
        print(f"{self.__nombre}({self.__x} , {self.__y})")
        
punto1 = Punto(10, 40)
punto1.ver_punto()

punto1.desplaza_x(5)
punto1.ver_punto()