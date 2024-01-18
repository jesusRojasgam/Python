print(f"Bueno,{nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")

numAleatorio = randint(1,100)
intentos = 0

for num in range(1,9):
    numUsuario = int(input(f"{nombre} elije un numero: "))
    if numAleatorio < 1 and numAleatorio > 100:
        print("ha elegido un número que no está permitido.")

    elif numAleatorio < numUsuario:
        print("es incorrecta has elegido un número mayor al número secreto.")

    elif numAleatorio > numUsuario:
        print("es incorrecta has elegido un número menor al número secreto.")
    else:
        print(f" ha ganado y {intentos} intentos te ha tomado")
        break

    if num <= 8:
        print(f"Te quedan {8 - num} intentos.")
if numUsuario != numAleatorio:
    print()




