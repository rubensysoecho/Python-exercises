num_dni = int(input("Introduce el número de DNI: "))

modulo_23 = num_dni % 23

if modulo_23 == 0:
    letra = "T"
elif modulo_23 == 1:
    letra = "R"
elif modulo_23 == 2:
    letra = "W"
elif modulo_23 == 3:
    letra = "A"
elif modulo_23 == 4:
    letra = "G"
elif modulo_23 == 5:
    letra = "M"
elif modulo_23 == 6:
    letra = "Y"
elif modulo_23 == 7:
    letra = "F"
elif modulo_23 == 8:
    letra = "P"
elif modulo_23 == 9:
    letra = "D"
elif modulo_23 == 10:
    letra = "X"
elif modulo_23 == 11:
    letra = "B"
elif modulo_23 == 12:
    letra = "N"
elif modulo_23 == 13:
    letra = "J"
elif modulo_23 == 14:
    letra = "Z"
elif modulo_23 == 15:
    letra = "S"
elif modulo_23 == 16:
    letra = "Q"
elif modulo_23 == 17:
    letra = "V"
elif modulo_23 == 18:
    letra = "H"
elif modulo_23 == 19:
    letra = "L"
elif modulo_23 == 20:
    letra = "C"
elif modulo_23 == 21:
    letra = "K"
elif modulo_23 == 22:
    letra = "E"
    
print("NIF -->", num_dni , letra)