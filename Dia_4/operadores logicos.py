# Inicializa la variable suma_cuadrados
suma_cuadrados = 0

# Itera a través de los números del 1 al 15 (inclusive)
for num in range(1, 16):
    # Calcula el cuadrado del número y suma al acumulador
    cuadrado = num ** 2
    suma_cuadrados += cuadrado

# Imprime el resultado
print("La suma de los cuadrados es:", suma_cuadrados)