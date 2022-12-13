dni = int(input("DNI sin letra: "))
modelo23 = dni % 23

# Substituir if por match (equivalente a switch de JAVA)
match modelo23:
    case 0:
        nif = str(dni) + "T"
    case 1:
        nif = str(dni) + "R"
    case 2:
        nif = str(dni) + "W"
    case 3:
        nif = str(dni) + "A"
    case 4:
        nif = str(dni) + "G"
    case 5:
        nif = str(dni) + "M"
    case 6:
        nif = str(dni) + "Y"
    case 7:
        nif = str(dni) + "F"
    case 8:
        nif = str(dni) + "P"
    case 9:
        nif = str(dni) + "D"
    case 10:
        nif = str(dni) + "X"
    case 11:
        nif = str(dni) + "B"
    case 12:
        nif = str(dni) + "N"
    case 13:
        nif = str(dni) + "J"
    case 14:
        nif = str(dni) + "Z"
    case 15:
        nif = str(dni) + "S"
    case 16:
        nif = str(dni) + "Q"
    case 17:
        nif = str(dni) + "V"
    case 18:
        nif = str(dni) + "H"
    case 19:
        nif = str(dni) + "L"
    case 20:
        nif = str(dni) + "C"
    case 21:
        nif = str(dni) + "K"
    case 22:
        nif = str(dni) + "E"

print("NIF:", nif)      
