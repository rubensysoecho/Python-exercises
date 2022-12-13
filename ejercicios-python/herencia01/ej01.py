class Mascota:
    
    __IVA = 1.21
    
    def __init__(self, nombre, num_patas, raza, precio_sin_IVA, color):
        self.__nombre = nombre
        self.__num_patas = num_patas
        self.__raza = raza
        self.__precio_sin_IVA = precio_sin_IVA
        self.__color = color

    def getNombre(self):
        return self.__nombre
        
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getNumPatas(self):
        return self.__num_patas
    
    def setNumPatas(self, num):
        self.__num_patas = num
        
    def getRaza(self):
        return self.__raza
    
    def setRaza(self, raza):
        self.__raza = raza
        
    def getColor(self):
        return self.__color
    
    def setColor(self, color):
        self.__color = color
    
    def pvp(self):
        return self.__precio_sin_IVA * self.__IVA
        
    def verDatos(self):
        print("Nombre:", self.__nombre)
        print("Nº Patas:", self.__num_patas)
        print("Raza:", self.__raza)
        print("PVP:", self.pvp())
        print("Color:", self.__color)
        
class Perro(Mascota):
    
    def __init__(self, nombre, raza, patita, precio_sin_IVA, color, num_patas = 4):
        super().__init__(nombre, num_patas, raza, precio_sin_IVA, color)
        self.patita = patita

    def verDatos(self):
        super().verDatos()
        print(f"Patita: {self.patita}")

class Loro(Mascota):
    
    def __init__(self, nombre, raza, habla, precio_sin_IVA, color, num_patas = 2):
        super().__init__(nombre, num_patas, raza, precio_sin_IVA, color)
        self.habla = habla
        
    def verDatos(self):
        super().verDatos() 
        print(f"Habla: {self.habla}")
    
perro1 = Perro("Lucky", "bóxer", True, 380, "Marrón")
loro1 = Loro("Andresito", "cacatúa", True, 110, "Verde")

print("IVA Perro ->", perro1.pvp())
print("IVA Loro ->", loro1.pvp())

print()

perro1.verDatos()
print()
loro1.verDatos()