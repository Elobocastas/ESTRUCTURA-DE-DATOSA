
A = [
    [4, 7, 2, 9, 5, 7],
    [1, 3, 7, 6, 8, 0],
    [9, 2, 5, 7, 4, 6],
    [8, 7, 1, 3, 7, 2],
    [5, 0, 6, 4, 2, 9],
    [7, 8, 9, 2, 1, 7]
]

def buscar_numero(valor):
    listaCoordenadas = []
    
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == valor:
                listaCoordenadas.append((i+1, j+1))
                
    if listaCoordenadas == []:
        return "No se encongro"
    else:
        return listaCoordenadas


valores_prueba = [7, 2, 9, 0, 4, 1, 6, 8, 3, 10]

print("Resultados de las 10 pruebas:") 

for numero in valores_prueba:
    resultado = buscar_numero(numero)
    print("X =", numero, "->", resultado)