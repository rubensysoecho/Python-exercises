opcion = (input("A.- Bicicleta\nB.- Moto o coche\nC.- Camion\n"))

if opcion == "A" or opcion == "a":
    print("BICICLETA")
    km = input("Número de km recorridos: ")
    km = float(km)
    print("El importe a pagar de la bicicleta es de", km, "euros")
elif opcion == "B" or opcion == "b":
    print("MOTO / COCHE")
    km = input("Número de km recorridos: ")
    km = float(km)
    print("El importe a pagar del coche o moto es de", km * 0.25, "euros")
elif opcion == "C" or opcion == "c":
    print("CAMIÓN")
    km = input("Número de km recorridos de más: ")
    km = float(km)
    peso = input("Tonelada de peso: ")
    peso = float(peso)
    print("El importe a pagar del camión es de", (0.25 * km) + (0.15 * peso), "euros")
else:
    print("Opcion incorrecta.")