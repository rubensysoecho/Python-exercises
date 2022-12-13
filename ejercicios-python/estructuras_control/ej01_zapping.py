canalSalida = int(input("Canal de salida: "))
canalObjetivo = int(input("Canal objetivo: "))

ordenLineal = canalObjetivo - canalSalida
ordenReverso = 99 - canalObjetivo + canalSalida

if canalSalida > canalObjetivo:
    ordenLineal = canalSalida - canalObjetivo
    ordenReverso = 99 - canalSalida + canalObjetivo
    if ordenLineal < ordenReverso:
        print("Salida:", ordenLineal)
    else:
        print("Salida:", ordenReverso)
else:
    if ordenLineal < ordenReverso:
        print("Salida:", ordenLineal)
    else:
        print("Salida:", ordenReverso)