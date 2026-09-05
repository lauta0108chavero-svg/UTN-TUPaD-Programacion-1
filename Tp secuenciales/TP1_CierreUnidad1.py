#PUNTO 1
nombre = input(" Coloque su nombre por favor : ")
print ("mucho gusto " + nombre )
numero1 = int(input(" ingrese su peso :"))
numero2 = float(input("ingrese su altura : "))
potencia = numero2 ** 2
print("El numero2 potenciado da : " , potencia )
cuenta = (potencia ) / (numero1)
print(" el resultado es : " , cuenta )

#Punto2



Numero_entero = input (" Por favor , escribe un numero entero : ")
Numero_entero = int (Numero_entero)
print (" El numero entero que ingresaste es :",Numero_entero)
Numero_decimal = input ("Ahora escribe un numero decimal :")
Numero_decimal = float (Numero_decimal)
print("El numero que ingresaste es : ", Numero_decimal)
suma = Numero_entero + Numero_decimal
print (" La suma de ambos numeros es :",suma)

#PUNTO3

nombre_completo = input (" Hola , ingrese su nombre completo por favor :")
print("Mucho gusto ,"+nombre_completo)
edad = input("¿Que edad tienes?")
nacionalidad = input("¿De que pais eres?")
print(" Tu nombre es "+ nombre_completo + " tienes " + edad + " y eres de " + nacionalidad)


#PUNTO4


nombre = input("¿Cual es tu nombre? : ")
print("Mucho gusto " + nombre )
numero1 = int(input("Coloque un numero en grados Celsius : "))
print("Su numero es : "  , numero1  )
fahrenheint = float(1.8)
Cuenta = float(fahrenheint) * int(numero1) 
print ( "El resultado es :", Cuenta + 32 )

#PUNTO5


print("Hola mundo")


#PUNTO6

nombre = input("Coloque su nombre por favor : ")
print("Mucho gusto ." + nombre )
numero = int(input("ingrese un numero : "))
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i }")


#PUNTO7



nombre = input ("¿ Cual es tu nombre ?")
print ("Mucho gusto : " + nombre )
numero1 = float (input("ingrese el primer numero :"))
numero2 = float (input("Ingrese el segundo numero : "))
numero3 = float (input("Ingrese el tercer numero :"))
promedio = (numero1 + numero2 + numero3) / 3
print (" El promedio es :" , promedio)


#PUNTO8



import math
radio = float (input("Ingrese el radio del circulo : "))
area = math.pi + radio**2
print("El area del circulo es : " , area )

radio = float (input("Ingrese el radio : "))
circunferencia = 2 * 3.1416 * radio 
print("La circunferencia es : " , circunferencia)



#PUNTO9


Nombre = input ("Coloque su nombre por favor : ")
print("¡Mucho gusto ! " + Nombre)
Segundos_totales = int(input("Introduce la cantidad de segundos : "))
# 3600 Segundos = 1 hora
Horas = Segundos_totales / 3600
print(f"{Segundos_totales} Segundos equivale a { Horas:2F} horas.")


#PUNTO10



nombre = input("cual es tu nombre : ")
print (" mucho gusto " , nombre )
numero1 = int(input(" ingrese el primer numero :"))
numero2 = int(input("ingrese el segundo numero  :"))
suma = numero1 + numero2 
resta = numero1 - numero2
Multiplicacion = numero1 * numero2
divicion = numero1 / numero2
print (" La suma es : " , suma )
print ("La resta es : " , resta )
print ("La multplicacion es :", Multiplicacion )
print ("La divicion es : ", divicion)



