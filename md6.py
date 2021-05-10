print("Por favor ingrese una cadena de caracteres")
dataStream = str(input())
if len(dataStream) > 0:
    print("Primer caracter: " + dataStream[0])
    print("Ultimo caracter: " + dataStream[len(dataStream) - 1])
    print("Tamaño de la cadena: " + str(len(dataStream)))
    print("Cadena en mayusculas: " + dataStream.upper())
    print("Cadena con espacion reemplazados: " + dataStream.replace(" ","**"))
    print("Cadena invertida: " + dataStream[::-1])
else:
    print("La cadena tiene qe tener al menos 1 character para qe funcione la aplicacion")