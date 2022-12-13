class Punto:
    
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
        
class Circulo:
    
    __pi = 3.14159
    
    def __init__(self, punto, radio):
        self.__punto = punto
        self.__radio = radio
        
    def area(self):
        return self.__pi * (self.__radio * self.__radio)
        

punto = Punto(10, 20)

circulo = Circulo(punto, 4.5)
print("Área del circulo ->", circulo.area())