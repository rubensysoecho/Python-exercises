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
        print(f"Punto: {self.__nombre}({self.__x} , {self.__y})")
        
class Circulo:
    
    __pi = 3.14159
    
    def __init__(self, punto, radio):
        self.__punto = punto
        self.__radio = radio
        
    def area(self):
        return self.__pi * (self.__radio * self.__radio)
    
    def longitud(self):
        return 2 * self.__pi * self.__radio
    
    def desplaza_x(self, num):
        self.__punto.desplaza_x(num)
    
    def desplaza_y(self, num):
        self.__punto.desplaza_y(num)
        
    def setRadio(self, num):
        self.__radio = num
        
    def ver_datos(self):
        self.__punto.ver_punto()
        print("Radio ->", self.__radio)

punto = Punto(20, 30)

circulo = Circulo(punto, 6)
print("Longitud ->", circulo.longitud())
circulo.desplaza_x(10)
circulo.ver_datos()
circulo.setRadio(7.5)
circulo.ver_datos()