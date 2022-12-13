class Encuesta:
    
    def __init__(self, pregunta, votosA = 0, votosB = 0):
        self.__pregunta = pregunta
        self.__votosA = votosA
        self.__votosB = votosB
        
    def getPregunta(self):
        return self.__pregunta
    
    def getVotosA(self):
        return self.__votosA
    
    def getVotosB(self):
        return self.__votosB
    
    def incA(self):
        self.__votosA += 1
    
    def incB(self):
        self.__votosB += 1
        
    def total_votos(self):
        return self.__votosA + self.__votosB
    
    def porcentajeA(self):
        if self.total_votos() != 0:
            return (self.__votosA / self.total_votos()) * 100
        else:
            return 0
    
    def porcentajeB(self):
        if self.total_votos() != 0:
            return (self.__votosB / self.total_votos()) * 100
        else:
            return 0
        
encuesta = Encuesta("¿Que país tiene mejor gastronomía, España o Italia?", 55, 30)
print("Porcentaje de voto a España -->", round(encuesta.porcentajeA(), 2), "%")
print("Porcentaje de voto a Italia -->", round(encuesta.porcentajeB(), 2), "%")

print()

encuesta.incA()
encuesta.incB()

print(encuesta.getPregunta())
print("Total de votos -->", encuesta.total_votos())
print("Votos a España -->", encuesta.getVotosA())
print("Votos a Italia -->", encuesta.getVotosB())
print("Porcentaje de voto a España -->", round(encuesta.porcentajeA(), 2), "%")
print("Porcentaje de voto a Italia -->", round(encuesta.porcentajeB(), 2), "%")