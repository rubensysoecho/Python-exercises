numeros = [1, 2, 3, 9, 2, 6, 10, 2, 2, 5]

num_buscado = int(input("Introduce el número a buscar: "))
veces_encontrado = numeros.count(num_buscado)

print(f"El número {num_buscado} se encuentra {veces_encontrado} veces en la lista.")