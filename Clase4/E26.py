from random import randint

def llenarAleatorio():
    n = randint(1,10)
    tabla = []
    for i in range(n):
        tabla.append([])
        n2 = randint(1,10)
        for j in range(n2):
            tabla[i] += [randint(1,10)]
    return tabla

def imprimir(tabla):
    for i in tabla:
        print("[",end="")
        for j in i:
            print("%4s"%j, end="")
        print("   ]")


tabla = llenarAleatorio()
imprimir(tabla)