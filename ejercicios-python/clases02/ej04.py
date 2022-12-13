class Empleado:
    
    def __init__(self, dni, nombre, apellidos, salario):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.salario = salario
    
    def __init__(self, dni):
        self.dni = dni
    
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre
        
    def salario_neto(self):
        return self.salario * 0.88
        
empleado = Empleado("12789671W", "Pepe", "Rodriguez", 1200)

print(empleado.salario_neto())