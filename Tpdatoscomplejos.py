#Punto1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
precios_frutas ["Naranja"] = 1200
precios_frutas ["Manzana"] = 1500
precios_frutas ["Pera"] = 2300
print (precios_frutas)

#Punto2
precios_frutas= {"Banana":1200 , "Anana":2500 , "Melon":3000 , "Uva":1450 , "Naranja":1200 , "Manzana":1500 , "Pera": 2300}
precios_frutas.update({
    'Banana': 1330,
    'Manzana': 1700,
    'Melón': 2800
})

print("2) Diccionario con los precios actualizados:")
print(precios_frutas)

#Punto 3

precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva':
1450 , "Naranja" : 1200 , "Manzana" : 1700 , "Pera" : 2300 }
print(precios_frutas.keys())

#Punto4

telefonos = {}
for i in range (5) :
    nombre = input("Ingrese su nombre :")
    numero = input ("Ingrese un numero :")
    telefonos[nombre] = numero
nombre  = input("Ingrese un nombre para buscar :")
if nombre in telefonos :
    print("El numero es :" , telefonos[nombre])
else:
    print("El contacto no existe")

   #Punto 5

frase = input("Ingrese una frase : ")
palabras = frase.split()
unicas = set(palabras)
cantidad = {}
for palabra in palabras :
    if palabra in cantidad :
        cantidad [palabra] += 1
    else :
        cantidad [palabra] = 1
print("Palabras unicas :" , unicas)
print("Cantidad de palabra :" , cantidad )  

#Punto 6
# Diccionario para almacenar los datos
alumnos = {}

# Lectura de datos de los 3 alumnos
for i in range(3):
    nombre = input(f"\nIngrese el nombre del alumno {i+1}: ")
    
    # Se solicitan las 3 notas
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    
    # Guardamos las notas en una tupla
    alumnos[nombre] = (n1, n2, n3)

# Cálculo y muestra de promedios
print("\n--- Resultados ---")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Alumno: {nombre} | Promedio: {promedio:.2f}")

    #Punto 7

# Definición de los conjuntos de ejemplo (puedes cambiarlos)
parcial_1 = {"Ana", "Pedro", "Luis", "María", "Juan"}
parcial_2 = {"Luis", "María", "Carlos", "Sofía", "Juan"}

# 1. Aprobaron ambos parciales (Intersección)
ambos = parcial_1.intersection(parcial_2)

# 2. Aprobaron solo uno de los dos (Diferencia simétrica)
solo_uno = parcial_1.symmetric_difference(parcial_2)

# 3. Lista total de aprobados sin repetir (Unión)
total_aprobados = parcial_1.union(parcial_2)

# Mostrar resultados
print("--- RESULTADOS DE LOS PARCIALES ---")
print(f"Aprobaron ambos parciales: {ambos}")
print(f"Aprobaron solo uno de los dos: {solo_uno}")
print(f"Total de estudiantes que aprobaron al menos uno: {total_aprobados}")

#Punto 8 

#Inicializamos el diccionario con algunos productos de ejemplo
inventario = {
    "manzanas": 50,
    "bananas": 30,
    "naranjas": 20
}

while True:
    print("\n--- GESTIÓN DE INVENTARIO ---")
    print("1. Consultar stock")
    print("2. Agregar unidades a un producto existente")
    print("3. Agregar un nuevo producto")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == "1":
        # • Consultar el stock de un producto ingresado
        producto = input("Ingrese el nombre del producto a consultar: ").lower()
        if producto in inventario:
            print(f"El stock actual de '{producto}' es: {inventario[producto]} unidades.")
        else:
            print(f"El producto '{producto}' no existe en el inventario.")
            
    elif opcion == "2":
        # • Agregar unidades al stock si el producto ya existe
        producto = input("Ingrese el nombre del producto a modificar: ").lower()
        if producto in inventario:
            cantidad = int(input("¿Cuántas unidades desea sumar?: "))
            if cantidad > 0:
                inventario[producto] += cantidad  # Suma las nuevas unidades al stock existente
                print(f"Stock actualizado. Nuevo stock de '{producto}': {inventario[producto]} unidades.")
            else:
                print("Por favor, ingrese una cantidad mayor a 0.")
        else:
            print(f"El producto '{producto}' no existe. Si es nuevo, use la opción 3.")
            
    elif opcion == "3":
        # • Agregar un nuevo producto si no existe
        producto = input("Ingrese el nombre del nuevo producto: ").lower()
        if producto not in inventario:
            cantidad = int(input(f"Ingrese el stock inicial para '{producto}': "))
            if cantidad >= 0:
                inventario[producto] = cantidad  # Crea la nueva clave-valor en el diccionario
                print(f"Producto '{producto}' registrado con éxito con {cantidad} unidades.")
            else:
                print("El stock inicial no puede ser negativo.")
        else:
            print(f"El producto '{producto}' ya existe. Si quiere sumarle stock, use la opción 2.")
            
    elif opcion == "4":
        print("¡Gracias por usar el sistema de inventario!")
        break  # Rompe el bucle para finalizar el programa
        
    else:
        print("Opción no válida. Por favor, elija un número del 1 al 4.")


  #Punto 9

# 1. Creación de la agenda vacía
agenda = {}

# 2. Agregar eventos usando una tupla (día, hora) como clave
agenda[("2026-09-14", "09:00")] = "Reunión de equipo"
agenda[("2026-09-14", "14:30")] = "Clínica médica"
agenda[("2026-09-15", "11:00")] = "Presentación de proyecto"

# 3. Función para consultar un evento específico
def consultar_evento(dia, hora):
    clave = (dia, hora)
    # .get() evita que el programa falle si la fecha/hora no existen
    return agenda.get(clave, "No hay eventos programados.")

# --- Ejemplos de uso ---

# Mostrar toda la agenda
print("--- Mi Agenda ---")
for (dia, hora), evento in agenda.items():
    print(f"El {dia} a las {hora}: {evento}")

print("\n--- Consulta Individual ---")
# Consulta de un evento existente
print(consultar_evento("2026-09-14", "09:00"))

# Consulta de un horario libre
print(consultar_evento("2026-09-14", "11:00"))


#Punto 10

# Diccionario original (País -> Capital)
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

# Inversión del diccionario usando dict comprehension
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

# Resultado
print(capitales_paises)