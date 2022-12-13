litrospiscina1 = int(input("Litros piscina (yo): "))
litrosbarrenho1 = int(input("Litros barreño (yo): "))
litrosperdidos1 = int(input("Litros perdidos (yo): "))
litrosllenados1 = 0
viajes1 = 0


litrospiscina2 = int(input("Litros piscina (vecino): "))
litrosbarrenho2 = int(input("Litros barreño (vecino): "))
litrosperdidos2 = int(input("Litros perdidos (vecino): "))
litrosllenados2 = 0
viajes2 = 0

posible = True
if litrosperdidos1 < litrosbarrenho1:
    while litrosllenados1 < litrospiscina1:
        litrosllenados1 += litrosbarrenho1
        litrosllenados1 -= litrosperdidos1
        viajes1 += 1
else:
    posible = False  

if litrosperdidos2 < litrosbarrenho2:
    while litrosllenados2 < litrospiscina2:
        litrosllenados2 += litrosbarrenho2
        litrosllenados2 -= litrosperdidos2
        viajes2 += 1
else:
    posible = False

if posible:
    if viajes1 < viajes2:
        print("YO", viajes1)
    elif viajes1 > viajes2:
        print("VECINO", viajes2)
    else:
        print("EMPATE", viajes1)
else:
    if viajes1 == 0:
        print("VECINO", viajes2)
    elif viajes2 == 0:
        print("YO", viajes1)