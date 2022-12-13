num_legio = int(input("Número de legionarios disponibles: "))
numEscudos = 0

while num_legio > 0:
    legio_esquina = 1;
    while ((legio_esquina + 1) * (legio_esquina + 1)) <= num_legio:
        legio_esquina += 1
    if legio_esquina == 1:
        numEscudos += 5
    else: numEscudos += (legio_esquina * 4) + (legio_esquina * legio_esquina)
    num_legio -= (legio_esquina * legio_esquina)
 
print("Número de escudos🛡 -->", numEscudos)
