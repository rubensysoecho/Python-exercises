def nota_media(notas):
    return sum(notas)/len(notas)

num_alumnos = int(input("Número de alumnos en el curso: "))

notas=[]
for i in range(0, num_alumnos):
    notas.append(float(input(f"Nota media del alumno {i + 1}: ")))

print("Nota media del curso --> ", nota_media(notas))