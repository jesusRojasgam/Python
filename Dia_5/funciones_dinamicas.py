#precios_cafe = [("capuchino",1.5),("expresson",1.2),("moka",1.9)]

#for cafe,precio in precios_cafe:
#    print(cafe)

precios_cafe = [("capuchino",1.5),("expresson",2),("moka",1.9)]

def cafe_mas_caros(lista_precios):
    precio_mas_caro=0
    cafe_mas_caros = ""

    for cafe,precio in precios_cafe:
        if precio > precio_mas_caro:
            precio_mas_caro= precio
            cafe_mas_caros=cafe
        else:
            pass


    return (cafe_mas_caros,precio_mas_caro)

cafe,precio = cafe_mas_caros(precios_cafe)

print(cafe_mas_caros(precios_cafe))
print(f"el cafe mas caro es {cafe} cuyo precio es {precio}")