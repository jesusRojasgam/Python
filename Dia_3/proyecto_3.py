texto = input("ingrese el texto que desee analizar: ")
letra1= input("ingrese la primera letra que deseas buscar: ")
letra2= input("ingrese la segunda letra que deseas buscar: ")
letra3= input("ingrese la tercera letra que deseas buscar: ")

minus= texto.lower()
letras= [letra1,letra2,letra3]

count1= minus.count(letra1)
count2= minus.count(letra2)
count3= minus.count(letra3)

print(f"Hola hemos contado tu primera letra, y se repite {count1} veces , de la segunda letra {count2} veces, y de la tercera letra {count3} veces")


textoSeparado = texto.split(" ")
cantidadPalapras = len(textoSeparado)

print(f"tambien encontramos que el texto tiene {cantidadPalapras} palabras")

print(f"la primera letra del texto es {texto[:1]}")
print(f"la ultima letra del texto es {texto[-1]}")


rever = list(reversed(textoSeparado))
unir =" ".join(rever)
print(unir)
#buscar = textoSeparado.find("python")

buscar = "python" in texto
if buscar == True:
    print("se encontro python en el texto")
else:
    print("no se encontro python en el texto")