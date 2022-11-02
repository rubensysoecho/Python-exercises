altura = input("Altura(cm): ")
edad = input("Edad: ")

k = 4

altura = float(altura)
edad = float(edad)

lorentz = altura - 100 - (((altura - 150) / 4) + ((edad - 20) / k))

perroult = altura - 100 + (edad * 10 - 90)

brocca = altura - 100

MLIC = 50 + 0.75 * (altura - 150)

print("Fórmula de Lorenzt -->", lorentz)
print("Fórmula de Perroult -->", perroult)
print("Índice de Brocca -->", brocca)
print("Fórmula del MLIC -->", MLIC)