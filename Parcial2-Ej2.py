print("Ingrese la cadena 1")
cadena1 = input()
print("Ingrese la cadena 2")
cadena2 = input()

print("Reemplazado de espacion en blanco:")
print(cadena1.replace(" ", "**"))

print("Cadena mas corta:")
if len(cadena1) <= len(cadena2):
    print(cadena1)
else:
    print(cadena2)

if len(cadena1) > 0:
    reemplazado = "&" + cadena1[1 : len(cadena1) - 1] + "&"
    print("Cadena 1 con caracteres reemplazados:")
    print(reemplazado)
else:
    print("La cadena 1 no tiene caracteres con lo cual no pueden reemplazarse")

if len(cadena2) > 0:
    reemplazado = "&" + cadena2[1 : len(cadena2) - 1] + "&"
    print("Cadena 2 con caracteres reemplazados:")
    print(reemplazado)
else:
    print("La cadena 2 no tiene caracteres con lo cual no pueden reemplazarse")