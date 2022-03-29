from random import randint
a = 0
v = True
print("-----Bienvenido-----\nResuelve las operaciones presentadas, si fallas se acaba el juego")
while v:
    opc = randint(1,2)
    num1 = randint(1,10) 
    num2 = randint(1,10)
    if(opc == 1):
        res = num1 * num2
        resUsuario = int(input(str(num1)+" * "+str(num2)+" = "))
        if(res == resUsuario):
            #print("¡Correcto!")
            a = 0
        else:
            print("Incorrecto :(\nLa respuesta es", res)
            v = False
    elif(opc == 2):
        res = num1 // num2
        resUsuario = int(input(str(num1)+" / "+str(num2)+" = "))
        if(res == resUsuario):
            a = 0
            #print("¡Correcto!")
        else:
            print("Incorrecto :(\nLa respuesta es", res)
            v = False
    #print()