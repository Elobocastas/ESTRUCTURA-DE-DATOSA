
TONELADAS_CARNITAS = [12, 24, 16, 15, 20, 18, 6, 10, 12, 11, 15, 12]

suma = 0 

for i in TONELADAS_CARNITAS:
    suma = suma + i  


promedio = suma / len(TONELADAS_CARNITAS)

print("Este es el promedio:", promedio)



MAYORES = []
MENORES = []
for i in TONELADAS_CARNITAS:
  if i > promedio:
     MAYORES.append(i)
  else:
    MENORES.append(i)

      





print ("Estos son los valores superiores", MAYORES)     
print ("Estos son los valores inferiores", MENORES)     