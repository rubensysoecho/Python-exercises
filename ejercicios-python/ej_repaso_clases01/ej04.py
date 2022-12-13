class Circunferencia:
    
    __PI = 3.14159
    
    def __init__(self, radio):
        if radio <= 0:
            print("ERROR. El radio debe ser mayor a 0.")
            self.__radio = ""
        else:
            self.__radio = radio
        
    def getRadio(self):
        return self.__radio
    
    def setRadio(self, radio):
        if radio <= 0:
            print("ERROR. El radio debe ser mayor a 0.")
        else:
            self.__radio = radio
        
    def setPi(self, pi):
        if pi < 3.14 or pi > 3.15:
            print("ERROR. PI debe oscilar entre 3.14 y 3.15")
        else:
            self.__PI = pi
        
    def area(self):
        return self.__PI * (self.__radio * self.__radio)
    
    def longitud(self):
        return self.__PI * 2 * self.__radio
    
    def ver_datos(self):
        if self.__radio != "":
            print("Radio ->", self.__radio)
            print("Area ->", self.area())
            print("Longitud ->", self.longitud())
        
        
circunferencia = Circunferencia(10)
circunferencia.ver_datos()
