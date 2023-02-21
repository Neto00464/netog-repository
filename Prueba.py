#Practica "Resumen de notas"

aprobados = 0
reprobados = 0
mayor = 0
menor = 150
while True:
    nota = float(input("Favor de ingresar la nota del estudiante: "))
    if nota >= 70:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1
    if nota > mayor:
        mayor= nota
    if nota < menor:
        menor= nota
    opcion= int(input("Desea seguir evaluando notas? (1-Si) (2-No) "))
    if opcion ==2:
        print(" Aprobados: ",aprobados,"\n","Reprobados: ",reprobados,"\n","Nota Mayor: ",mayor,"\n","Nota menor: ",menor) 
        break
        if while for else
