cal_alumnos =[8,8,7,5,10,9,9,5,6,10]


suma = 0 

for i in cal_alumnos:
    suma = suma + i  
    promedio = suma / len(cal_alumnos)

print (promedio)


Aprobado = []
Reprobado = []  
Sobresalientes = [] 
PA = 0
PB =0
n =0
m=0
S=0
for i in cal_alumnos:
    if i > promedio:
        Aprobado.append(i)
   
        if(i >= 7):
            n += 1

    if i > promedio:
        Sobresalientes.append(i)
        if(i >=10):
            S += 1        
    else:
        Reprobado.append(i) 
        if(i <= 7):
            m += 1

PA = len(Aprobado)/ 10 *100
PB = len(Reprobado)/ 10 *100
  
   


print("Aprobados",n)
print("reprobados",m)
print("sobresaliente",S)           
print(PA,"%")
print(PB,"%")