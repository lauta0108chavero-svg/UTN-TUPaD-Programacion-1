# PUNTO 1

for numero in range (0,101):
    print(numero)




 #PUNTO 2

nombre = input("coloca tu nombre : ")
print ("muvho gusto ", nombre )
numero = int(input("escribe un numero entero : "))

if numero < 0 :
    numero = - numero
contador = 0

if numero == 0:
    contador = 1
else :
    while numero > 0 :
        numero = numero // 10
        contador += 1    

print ("la cantidad de digitos es : ",contador) 




#PUNTO 3

num1 = int(input("ingrese el primer numero : "))
num2 = int(input("ingrese el segundo numero :"))

if num1 > num2 :
    num1 , num2 = num2 , num1
suma = 0 
for i in range (num1 + 1 , num2):
    suma += i

print ("la suma es : ",suma)




#PUNTO 4

suma = 0
numero = int(input("ingrese un numero entero (0 para terminar :)"))

while numero != 0 :
    suma += numero
    numero = int(input("ingrese otro numero entero (0 para terminar ):"))
print ("la suma total es : ", suma ) 


#PUNTO 5

import random
numero_secreto = int (input("adivina el numero (0 al 9) :"))
intentos = 0

while True :
    numero = int(input("adivina el numero( 0 al 9): "))
    intentos += 1

    if numero == numero_secreto :
        print (" Correcto ")
        print ("cantidad de intentos " , intentos )
        break
    else :
        print ("incorrecto , intenta nuevamente .")





   #PUNTO 6


for numero in range (100,-1,-2) :
    print(numero)   





  #PUNTO 7

nombre = input("Coloque su nombre por favor : ")
print("Mucho gusto ", nombre )
numero = int(input("Coloque un numero entero positivo :") )

suma = 0
for i in range (numero + 1) :
    suma = suma + i
print("la suma de los numeros entre 0 y ", numero , " es", suma ) 






#PUNTO 8
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range (5):
    numero = int(input("ingrese un numero entero :"))

    if numero % 2 == 0 :
        pares += 1
    else :
        impares += 1

    if numero > 0 :

        positivos += 1
    elif numero < 0 :
        negativos += 1 

print ("cantidad de numero pares :" ,pares)
print ("cantidad de numeros impares :", impares )
print ("cantidad de numero positivos : ", positivos )
print ("cantidad de numeros negtivos :" , negativos )




#PUNTO 9

cantidad = 5 # cambia este valor para probar 

suma = 0

for i in range (cantidad) :
    numero = int (input("ingese un numero entero : "))
    suma += numero

media = suma / cantidad 
print ("la media de los numeros ingresados es : " , media )


#PUNTO 10
nombre = input ("coloque su nombre pot favor : ")
print ("mucho gusto ", nombre )
numero = int (input ("ingrese un numero : "))

invertido = 0
while numero > 0 :
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10 

print ("numero invertido : ", invertido)