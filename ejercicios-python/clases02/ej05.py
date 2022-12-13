class NotasAlumno:
    
    def __init__(self, asignatura, nombre, apellidos, nota_eval1, nota_eval2, nota_eval3):
        self.__asignatura = asignatura
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__nota_eval1 = nota_eval1
        self.__nota_eval2 = nota_eval2
        self.__nota_eval3 = nota_eval3
        
    def getAsignatura(self):
        return self.__asignatura
    def getNombre(self):
        return self.__nombre
    def getApellidos(self):
        return self.__apellidos
    def getNotaEval1(self):
        return self.__nota_eval1
    def getNotaEval2(self):
        return self.__nota_eval2
    def getNotaEval3(self):
        return self.__nota_eval3
    
    def setAsignatura(self, valor):
        self.__asignatura = valor
    def setNombre(self, valor):
        self.__nombre = valor
    def setApellidos(self, valor):
        self.__apellidos = valor
    def setNotaEval1(self, valor):
        self.__nota_eval1 = valor
    def setNotaEval2(self, valor):
        self.__nota_eval2 = valor
    def setNotaEval3(self, valor):
        self.__nota_eval3 = valor
        
    def media(self):
        sumanotas = self.getNotaEval1 + self.getNotaEval2 + self.getNotaEval3
        return sumanotas / 3
    
    def verDatos(self):
        print("Asignatura ->", self.getAsignatura())
        print("Nombre ->", self.getNombre())
        print("Apellidos ->", self.getApellidos())
        print("Nota 1ª evaluacion ->", self.getNotaEval1())
        print("Nota 2ª evaluacion ->", self.getNotaEval2())
        print("Nota 3ª evaluacion ->", self.getNotaEval3())
        
notas_alumno = NotasAlumno("Lenguaje de marcas", "Andres", "Vieites Rodriguez", 6, 7.5, 8.6)

notas_alumno.verDatos()