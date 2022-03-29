lista = [1,"hola",3.5,False]

while len(lista) > 0:
    print (lista)
    elem = int(input("Ingrese la posición del elmento a eliminar: "))
    if elem < len(lista):
        del(lista[elem])
        print()
    else:
        print ("El elemento esta fuera del rango\n")
        continue