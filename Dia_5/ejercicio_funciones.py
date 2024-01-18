from random import choice

dado1 = ["1", "2", "3", "4", "5", "6"]
dado2 = ["1", "2", "3", "4", "5", "6"]


def azar(lista):
    choice(lista)
    return lista


print(azar(dado1))
print(azar(dado2))