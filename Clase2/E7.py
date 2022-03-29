from random import randint

zonaUsuario = int(input("¿En qué zona desea disparar? "))
zonaPortero = randint(1,6)

#radint(x,y) numero aleatorio entre "x" y "y"
#random() numero aleatorio entre 0 y 10
#randrange(x,y,p) numero aleatorio entre "x" y "y" con un paso de "p"
#uniform(x,y) numero aleatorio de tipo flotante entre "x" y "y"

print("La zona cubiertapor el portero es: ",zonaPortero)

if zonaPortero == zonaUsuario:
    print("No ha sido gol")
else:
    print("GOLAAAAAAAZOOOOOOOOOOOOO")