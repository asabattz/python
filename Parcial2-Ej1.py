# Funcion simple de ayuda para poder leer siempre un numero que no sea negativo
def leerEnteroPositivo():
    entero = -1
    while entero < 0:
        try:
            entero = int(input())
        except:
            entero = -1
        if entero < 0:
            print("El valor debe ser positivo diferente de cero y numerico")
    return entero

loop = True
cantidadDeRestaurantes = 0
restaurantesAltaRecaudacionSinDescuentos = 0

ingresoRestaurantMasBajo = -1
nombreRestaurantMasBajo = ""

restaurantesConIntermediaAltaRecaudacion = 0
comensalesEnIntermediaAltaRecaudacion = 0

while loop == True:
    print("Ingrese el nombre del restaurante")
    nombre = str(input())
    if (nombre.upper() == "FIN"):
        loop = False
        continue
    print("Ingrese la cantidad de comensales")
    comensales = leerEnteroPositivo()
    print("Ingrese total recaudado en pesos")
    recaudacion = leerEnteroPositivo()
    print("Ingrese total de descuentos aplicados en pesos")
    descuento = leerEnteroPositivo()
    
    cantidadDeRestaurantes += 1
    
    if descuento == 0 and recaudacion >= 2000000:
        restaurantesAltaRecaudacionSinDescuentos += 1
    
    if ingresoRestaurantMasBajo == -1 or recaudacion < ingresoRestaurantMasBajo:
        ingresoRestaurantMasBajo = recaudacion
        nombreRestaurantMasBajo = nombre
    
    if recaudacion > 500000:
        restaurantesConIntermediaAltaRecaudacion += 1
        comensalesEnIntermediaAltaRecaudacion += comensales

print("El porcentaje de restaurante que recaudaron al menos $2.000.000 de pesos sin descuentos es: " + str(restaurantesAltaRecaudacionSinDescuentos * 100 / cantidadDeRestaurantes) + "%")
print("El restaurante con menor ingreso es " + nombreRestaurantMasBajo + " con una recaudacion total de " + str(ingresoRestaurantMasBajo))
print("El promedio de comensales en los restaurantes que recaudaron mas de $500.000 es de " + str(comensalesEnIntermediaAltaRecaudacion / restaurantesConIntermediaAltaRecaudacion))