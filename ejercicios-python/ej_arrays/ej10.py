precios = [5, 5.5, 10, 300, 2.52, 2.5, 3, 8, 15, 20]

def media(lista):
    return sum(lista) / len(lista)

def num_menorqueX(lista, max):
    num = 0
    for i in range(0, len(lista)):
        if lista[i] < max: num += 1 
    return num

print("Mayor precio:", max(precios))
print("Menor precio:", min(precios))
print("Precio medio:", media(precios))
print("Nº Precios por debajo de 30:", num_menorqueX(precios, 30))