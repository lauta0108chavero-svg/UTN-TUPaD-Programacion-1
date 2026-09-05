
#Punto 1

notas = []

for i in range (10):
    nota = float (input("introduzca la nota del estudiante :"))
    notas.append(nota)

print("\nlista de notas : ", notas)

suma = 0 
for nota in notas :
    suma += nota
promedio = suma / len(notas)
print ("promedio : " , promedio) 

mayor = notas [0]
menor = notas [0]

for nota in notas :
    if nota > mayor :
        mayor = nota
    if nota < menor :
        menor = nota

print ("nota mas alta :" , mayor) 
print ("nota mas baja :" , menor)



#Punto 2

productos = []
for i in range ( 5 ):
    producto = input ("ingrese un producto : ")
    productos.append(producto)

print ("\nlista original :" ,productos)  
lista_ordenada = sorted(productos) 
print("lista ordenada :", lista_ordenada)

eliminar = input("\n ¿ que producto desea eliminar ? ")
if eliminar in productos :
    productos.remove(eliminar)
    print ("producto eliminado correctamente .")
else :
    print ("el producto no se encuentra en la lista .")
    print ("lista actualizada : " , productos)    



#Punto 3

import random
numeros = []
pares = []
impares = []

for i in range (15) :
    numero = random.randint ( 1, 100)
    numeros.append (numero)

for numero in numeros :
    if numero % 2 == 0:
        pares.append (numero)
    else :
        impares.append (numero)

print ("lista de numeros :", numeros)
print ("numeros pares : " , pares)
print(" numeros impares :", impares)

print ("cantidad de numeros pares :" , len(pares))
print (" cantidad de numeros impares :" , len(impares))



#Punto 4

lista = [1,3,5,3,7,1,9,5,3]
sin_repetidos = []

for numero in lista :
    repetido = False

    for elemento in sin_repetidos :
        if numero == elemento :
         repetido = True

    if repetido == False : 
        sin_repetidos.append(numero)

print ("lista original :" , lista)
print ("lista sin elememtos repetidos :",sin_repetidos)

#Punto 5
estudiantes = []

for i in range (8):
    nombre = input("ingrese el nombre del estudiante :")
    estudiantes.append(nombre)

print ("\n lista actual :" , estudiantes)

#Pregunta si queres agrgar o quitar un estudiante 
opcion = input("¿ desea agregar o eliminar un estudiante ? : ")
print(opcion)
if opcion == "agregar":
    nuevo = input ("ingrese el nombre del nuevo estudiante :")
    estudiantes.append(nuevo)
    print ("estudiante agregado correctamente .")

elif opcion == "eliminar":
    eliminar = input("ingrese el nombre del estudiante que desea eliminar :")

    if eliminar in estudiantes :
        estudiantes.remove(eliminar)
        print("estudiante eliminado correctamente ")

    else : 
        print (" el estudiante no se encuentra en la lista ")


else :
    print("opcion no valida ")
    

print ("lista final :" , estudiantes)


#Punto 6

numeros = []
for i in range (7) :
    numero = int(input("ingrese un numero : "))
    numeros.append(numero)

print ("lista orignal " , numeros) 

ultimo = numeros [6]

for i in range (6,0,-1):
    numeros[i] = numeros[i - 1]

numeros[0] = ultimo
print("lista rotada : ", numeros)    


#Punto 7

temperaturas = []

for i in range (7):
    minima = float (input("ingrese la temperatura minima del dia " + str ( i + 1) +":" ))
    maxima = float (input("ingrese la temperatura maxima del dia " + str ( i + 1) + ":"))
    temperaturas.append([minima, maxima ])

suma_minimas = 0
suma_maximas = 0

for i in range (7):
    suma_minimas += temperaturas [i][0]
    suma_maximas += temperaturas [i][1]

promedio_minimas = suma_minimas / 7
promedio_maximas = suma_maximas / 7

print (" \n Promedio de las temperaturas minimas :", promedio_minimas)
print ("\n Promedio  de las temperaturas maximas : ", promedio_maximas)


mayor_amplitud = temperaturas [0][1] - temperaturas [0][0]
dia_mayor = 1


for i in range (7):
    amplitud = temperaturas [i][1] - [i][0]
    if amplitud > mayor_amplitud :
        mayor_amplitud = amplitud 
        dia_mayor = i + 1


print("el dia con mayor amplitud termica fue el dia " , dia_mayor)
print (" la amplitud termica fue de ", mayor_amplitud ,"grados")



#Punto 8

notas = []

for i in range (5) :
    fila = []
    print("\n estudiante ", i + 1)
    
    for j in range (3):
        nota = float (input("ingrese la nota de la materia " + str ( j + 1 ) + ":"))
        fila.append(nota)

    notas.append (fila) 

print ("\npromedio de cada estudiante :")

for i in range (5):
    suma = 0
    for j in range (3):
        suma += notas [i] [j]
    promedio = suma / 3        
    print ("estudiante ", i + 1 , ":" , promedio )


print ("\npromedio de cada materia : ")
for j in range (3) :
    suma = 0 
    for i in range (5):
        suma += notas [i][j]
    promedio = suma / 5
    print("materia", j + 1 , ":" , promedio)



    #Punto 9
tablero = []

for i in range (3):
    fila = []

    for j in range (3):
        fila.append ("-")
    tablero.append(fila) 


for turno in range (9) :
    print ("\ntablero : ")
    for i in range (3) :
        print (tablero [i])

if turno % 2 == 0 :
    ficha = "x"
else :
    ficha = "o"
print ("\nturno del jugador " , ficha)

fila =int(input("ingrese la fila (0 , 1 o 1 : )"))
columna = int(input("ingrese la columna (0 , 1 o 2 : )"))

if tablero[fila][columna] == "-" :
    tablero [fila][columna] = ficha
else :
    print ("esa casilla ya esta ocupada ")
    turno -= 1


print("\ntablero final : ")
for i in range (3):
    print(tablero[i])




#Punto 10

ventas = []

for i in range (4):
    fila = []
    print ("\n producto" , i + 1)
    for j in range(7):
        venta = int(input("ingrese las ventas del dia " + str (j + 1 ) + ":" ))
        fila.append (venta)
    ventas.append (fila)


print ("\ntotal vendio por cada producto : ")
for i in range (4):
    total = 0 
    for j in range (7):
        total += ventas [i][j]
    print("producto" , i + 1 , "-" , total ) 




    mayor_venta_dia = 0
    dia_mayor = 0
    for j in range (7):
        total_dia = 0
        for i in range(4) : 
            total_dia += ventas [i][j]
        if total_dia > mayor_venta_dia :
            mayor_venta_dia = total_dia
            dia_mayor = j + 1 


print ("\nel dia con mayores ventas fue el dia " , dia_mayor )
print("ventas totales ese dia" , mayor_venta_dia)




mayor_producto = 0
productos_mas_vendido = 0
for i in range (4):
    total = 0
    for j in range (7):
        total += ventas [i][j]
    if total > mayor_producto :
        mayor_producto = total
        productos_mas_vendido += i + 1



print ("\nel producto mas vendido fue el producto " , productos_mas_vendido)
print ("total vendido : " , mayor_producto) 


