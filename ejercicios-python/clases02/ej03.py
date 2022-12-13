class Rectangulo:
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def perimetro(self):
        return 2 * self.altura + 2 * self.base
    
    def area(self):
        return self.base * self.altura
    
rectangulo = Rectangulo(7.5, 4.6)

print("Perimetro:", rectangulo.perimetro())
print("Area:", rectangulo.area())