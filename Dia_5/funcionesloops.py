

#def chequear_3_cifras(numero):
#    return  numero in range(100,1000)
#suma = 521 + 888
#resultado1 = chequear_3_cifras(suma)
#print(resultado1)

#def chequear_3_cifras(list):
#    list_3_cifras= []
#
#    for n in list:
#        if n in range(100,1000):
#            list_3_cifras.append(n)
#        else:
#            pass
#    return list_3_cifras
#
#resultado = chequear_3_cifras([555,99,600])
#print(resultado)

def suma_menores(lista):
    suma = []

    for n in lista:
        if n in range(0, 1000):
            suma.append(n)
        else:
            lista_numeros = sum(suma)
            print(lista_numeros)
    return suma


resultado = suma_menores([56, 1, 5994])
print(resultado)


