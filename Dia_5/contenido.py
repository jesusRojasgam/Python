def mi_funcion (nombre):
    '''es una funcion para crear ...'''
    print("hola"+nombre)

mi_funcion("juan")


def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")


bienvenida("julia")

def sumar (num1,num2):
    return  num1+num2


def invertir_palabra():
    mensaje = "Python"
    mayusculas = mensaje.upper()
    minusculas = mensaje.lower()
    print(mayusculas)
    print(minusculas)
    escritor = 'Fyodor Mikhailovich Dostoevsky'
    cadenaInvertida = escritor[::-1]
    print(cadenaInvertida)


def invertir_palabra():
    palabras = "Python"
    palabras.upper()
    palabras[::-1]

    return invertir_palabra


print(invertir_palabra())


def invertir_palabra(palabras):
    palabra = palabras.upper()[::-1]
    return palabra


print(invertir_palabra("Python"))
