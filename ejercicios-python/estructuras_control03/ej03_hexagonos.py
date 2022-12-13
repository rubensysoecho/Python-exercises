num = int(input("Numero de caracteres: "))
caracter = input("Caracter: ")

num_original = num

for i in range(num_original - 1):
    print(caracter * num)
    num += 2

for i in range(num_original):
    print(caracter * num)
    num -= 2