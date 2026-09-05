

#punto1

nombre = input("Ingrese su nombre por favor : ")
print (" Mucho gusto " , nombre )
edad = int(input("Ingrese su edad por favor : "))

if edad > 18 :
    print (" Es mayor de edad ")



#punto2
    
nombre = input (" Cual es tu nombre : ")
print ("Mucho gusto " , nombre )
nota = int(input (" Coloque su nota por favor : "))

if nota >= 6 :
    print (" Usted esta Aprobado ")

else :
    print("Usted esta Desaprobado ")




#punto3

nombre = input ("Coloque su nombre por favor : ")
print ("Mucho gusto " + nombre )
numero = int (input (" Coloque un numero par : "))

if numero %2==0 :
    print ("Ha ingresado un numero par ")

else :
    print("Por favor ingrese un numero par ")   





#punto4

nombre = input("Coloque su nombre por favor : ")
print("Mucho gusto " + nombre )
edad = int (input("Coloque su edad : "))

if edad < 12 :
    print (" Usted  es un niño/a ")

elif edad >= 12 and edad <= 18 :
    print ("Usted es un adolecente : ")

   
elif edad >= 18 and edad <= 30 :
    print ("Usted es un adulto/a joven ")

else :
    print ("Usted es un adulto/a ")




#punto5

nombre = input("Ingrese su nombre por favor : ")
print ("Muvho gusto " + nombre )

contraseña = (input("Ingrese su contraseña por favor : "))

if 8 <= len(contraseña) <= 14 :
    print("Su contraseña es correcta ")

else :
    print("Por favor , ingrese una contraseña de 8 y 14 caracteres ") 





#punto6

    import random
from statistics import mean , median , mode

numeros_aleatorios = [random.randint(1,100) for i in range (50)]

media = mean (numeros_aleatorios)
mediana = median (numeros_aleatorios) 
moda = mode (numeros_aleatorios)

print (f"media : {media :2f}")
print (f"mediana : {mediana :2f}")
print (f"moda : {moda} ")

if media > mediana > moda :
    print("Resultado : Sesgo positvo o a la derecha")
elif media < mediana < moda :
    print ("Resultado : Sesgo negativo o a la derecha ")
elif media == mediana == moda :
    print ("Resultado sin sego ")
else :
    print("Resultado : Los datos no representan un sesgo claro segun el criterio estricto ")






#punto7

nombre = input ("Coloque su nombre por favor : ")
print ("Mucho gusto , " + nombre )
frase = input("Coloque una palabra o frase : " )
vocales = ("  a , e , i , o , u ,A , E , I , O , U , Á , É , Í , Ó , Ú, á , é , í , ó , u")

if frase and frase[-1] in vocales :
    resultado = frase + "!"
else : 
    resultado = frase 
    print ("Resultado : " , resultado)



#punto8
nombre = input ("Coloque su nombre por favor : ")
print ("Elije una opcion : ")
print ("1. nombre en MAYUSCULAS ")
print ("2. nombre en minusculas ")
print ("3. nombre con la primera leta en mayuscula ")

opcion = input("Ingresa el numero de tu opcion 1 , 2 o 3: ")
if opcion == "1" :
    print("Tu nombre es : " , nombre.upper())

elif opcion == "2" : 
    print ("Tu nombre es : " , nombre.lower())

elif opcion == "3" :
    print("Tu nombre es : " , nombre.title())

else :
    print("Parece que no elegiste una opcion valida ")


#punto9

nombre = input ("Coloque su nombre por favor : ")
print ("Mucho gusto  : " , nombre )
magnitud = float (input("Coloque la magnitud del terremoto : "))

if magnitud >= 3 and magnitud <= 4 :
    print("El terremoto es muy leve ")

elif magnitud >= 4 and magnitud <= 5:
    print ("El terremoto es Leve ")

elif magnitud >= 5 and magnitud <= 6:
    print("El terremo es moderado , sentido por las personas pero geralmente no causa daño ")

elif magnitud >= 6 and magnitud <= 7 :
    print ("El terremoto ha sido fuerte , puede causar daños ")

elif magnitud < 7 : 
    print ("El terremoto ha sido muy fuerte y puede causar daños significativos ")
     
else :
    print ("Extremo y puede causar graves daños a gran escala ")





#punto10


hemisferio = input("¿ En que hemisferio se encuentra ? (N/S) ").upper()
mes = int ( input ("Ingrese el numero del mes (1-12): "))
dia = int ( input(" Ingrese el dia : "))

if( mes == 12 and dia >= 21 ) or mes in [1 , 2] or (mes == 3 and dia <= 20 ):
    estacion_norte = "Invierno "
elif(mes == 3 and dia >= 21 ) or mes in [4 , 5 ] or (mes == 6 and dia <= 20 ):
    estacion_norte = "Primavera"
elif(mes == 6 and dia >= 21 ) or mes in [7 , 8 ] or (mes == 9 and dia <= 20 ):
    estacion_norte = "Verano"
else :
    estacion_norte = "Otoño"


