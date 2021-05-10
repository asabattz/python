def encontrarNumeroAmigo(numero):
    numeroAmigo = 0
    for i in range(int(numero / 2) + 1, 0, -1):
        if numero % i == 0:
            numeroAmigo += i
    return numeroAmigo

def sonAmigos(numero1, numero2):
    if encontrarNumeroAmigo(numero1) == numero2 and numero1 == encontrarNumeroAmigo(numero2):
        return True
    else:
        return False

numero1 = int(input("Ingrese el primero numero:"))
numero2 = int(input("Ingrese el segundo numero:"))

if numero1 <= 0 or numero2 <= 0:
    print("Error, los numeros deben ser positivos mayores que 0")
elif sonAmigos(numero1, numero2):
    print(f"Los numero {numero1} y {numero2} son amigos!")
else:
    print(f"Los numero {numero1} y {numero2} NO son amigos!")