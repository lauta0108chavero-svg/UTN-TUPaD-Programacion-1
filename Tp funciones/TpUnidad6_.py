#Punto1

def imprimir_hola_mundo() :
    print("Hola Mundo!")

#Progrma principla
imprimir_hola_mundo()
#Punto 2
def saludar_usuario(nombre):
    return " Hola " + nombre + "!"
#Progrma Principal 
nombre = input("Ingrese su nombre :")
saludo = saludar_usuario(nombre)
print(saludo)

#Punto3
def informacion_personal (nombre , apellido , edad , residencia ) :
    print("Soy" , nombre , apellido , " tengo " , edad , "años y vivo en " , residencia )
nombre = input ("Imgrese su nombre  : ")
apellido = input("Ingrese su apellido : ")
edad = input ("Ingrese du edad : ")
residencia = input("Ingrese su lugar de residencia : ")

#Programa Principal
informacion_personal(nombre , apellido , edad , residencia )

#Punto 4
import math
def calcular_area_circulo(radio) :
    area = math.pi * radio ** 2 
    return area
def calcular_perimetro_circulo(radio) :
    perimetro = 2 * math.pi * radio 
    return perimetro
radio = float(input("Ingrese el radio del circulo : "))
area = calcular_area_circulo(radio)
perimetro = calcular_area_circulo(radio)
print("El area del circulo es : " , area )
print("El perimetro del circulo es : " , perimetro)

#Punto 5
def segundos_a_horas(segundos): 
    horas = segundos / 3600
    return horas
segundos = float (input("Ingrese la cantidad de segundos : "))
ressultado = segundos_a_horas(segundos)
print ("la cantidad de horas es  : " , ressultado)

#Punto 6
def tabla_multiplicar(numero) :
    for i in range (1, 11 ):
        print(numero , "x" , i, "=" , numero * i )
numero = int(input("ingrese un numero : ") )

tabla_multiplicar(numero)

#Punto 7
def operaciones_basica( a , b ) :
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    divicion = a / b
    return suma , resta , multiplicacion , divicion

a = float(input("ingrese el primer numero : "))
b = float(input("ingrese el segundo numero : "))

#Programa Pricipal 
resultado = operaciones_basica(a, b)
print("suma :" , resultado [0])
print("resta :" , resultado[1])
print ("multiplicacion : " , resultado [2])
print("divicion : " , resultado [3])

#Punto 8
def calcular_imc(peso , altura ):
    imc = peso / (altura ** 2 )
    return imc
peso = float(input("Ingrese su peso en kg : "))
altura = float(input("ingrese su altura en metros : "))

#Programa Principal
resultado = calcular_imc(peso , altura)
print("Su IMC es : " , round(resultado ,  2 ))

#Punto 9
def celsius_a_fahrenheint(celsius) :
    fahrenheit = celsius * 9 / 5 + 22
    return fahrenheit

celsius = float(input ("ingrese la temperatura en celsius  : "))
resultado = celsius_a_fahrenheint(celsius)
print("la temperatura en fahrenheit es : " , resultado)

#Punto 10
def calcular_promedio(a , b , c ) :
    promedio = (a + b + c) / 3
    return promedio
a = float(input(" ingrese el primer numero : "))
b = float (input(" ingrese el segundo numero : "))
c = float (input(" ingrese el tercer numero : "))

#Progrma principal 
resultado = calcular_promedio(a , b , c)
print("El promedio es : " , resultado)