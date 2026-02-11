Arreglo = [1, 2, 4, 4, 4, 5, 7, 9, 11, 11, 13, 14, 15, 16, 16]
Sin_iguales = []

for i in Arreglo:
 if i not in Sin_iguales:
        Sin_iguales.append(i)

print("Lista sin iguales:",Sin_iguales)