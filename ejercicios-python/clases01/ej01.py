class Coche:
    
    def __init__(self, modelo, pasajeros, deposito, kpl):
        self.modelo = modelo
        self.pasajeros = pasajeros
        self.deposito = deposito
        self.kpl = kpl
    
    def calcularAutonomia(self):
        return self.deposito * self.kpl
    
    def mayorAutonomia(self, c):
        if self.calcularAutonomia > c.calcularAutonomia:
            return True
        else:
            return False

coche1 = Coche("Renault x", 5, 60, 20)
coche2 = Coche("Mercedes v", 7, 90, 30)

print(f"Tiene {coche1.modelo} más autonomía que {coche2.modelo}? {coche1.mayorAutonomia(coche2)}")