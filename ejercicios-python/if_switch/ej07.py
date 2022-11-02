caracter1 = input("Carácter 1: ")
caracter2 = input("Carácter 2: ")
caracter3 = input("Carácter 3: ")

caracteres = [caracter1, caracter2, caracter3]

if caracteres == sorted(caracteres):
    print("Los carácteres se encuentran en orden alfabético.")
else:
    print("Los carácteres NO se encuentran en orden alfabético")