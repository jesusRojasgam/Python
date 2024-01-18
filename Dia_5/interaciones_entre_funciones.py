from random import shuffle
#lista inicial
palitos= ["-","--","---","----"]

#mezclar palitos
def mix(lista):
    shuffle(lista)
    return lista

print(mix(palitos))
#pedirle intento
def probar_suerte():
    intento = ""

    while intento not in ["1","2","3","4"]:
        intento = input("elije un numero del 1 al 4: ")

    return int(intento)
#intento1=probar_suerte()
#print(intento1)

#comprobar intento

def chequear_intentos(lista,intento):
    if lista[intento -1] == "-":
        print("Haz perdido")
    else:
        print("te salvaste")

    print(f"te ha tocado{lista[intento-1]}")


palitos_mezclados = mix(palitos)
seleccion = probar_suerte()
chequear_intentos(palitos_mezclados,seleccion)