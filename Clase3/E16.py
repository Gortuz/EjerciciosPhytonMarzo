from random import randint

def ppt(op):
    if(op == 1):
        r = "piedra"
    if(op == 2):
        r = "papel"
    if(op == 3):
        r = "tijera"
    return r

victorias = 0
victoriasPC = 0
print()
while victorias < 3 and victoriasPC < 3:
    print("Opciones:\n1.- Pieda\n2.- Papel\n3.- Tijera")
    opUsuario = int(input("Opción: "))
    if(opUsuario > 3 or opUsuario < 1):
        print("Ingrese una opción valida")
        continue
    opMaquina = randint(1,3)
    print("La maquina eligió: ",ppt(opMaquina))
    print("La usuario eligió: ",ppt(opUsuario))

    if(opUsuario == 1 and opMaquina == 3)or(opUsuario == 2 and opMaquina == 1) or (opUsuario == 3 and opMaquina == 2):
        print("Gana el usuario")
        victorias += 1
    elif(opUsuario == opMaquina):
        print("Es un empate")
    else:
        print("Gana la máquina")
        victoriasPC+=1
        
    print("Número de victorias usuario: ",victorias)
    print("Número de victorias pc: ",victoriasPC)

    print()

if(victorias == 3):
    print("Ganó el usuario")
else:
    print("Ganó la máquina")
