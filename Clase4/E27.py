
def imprimir(tabla):
    print("")
    for i in tabla:
        print("[",end="")
        for j in i:
            print("%3s"%j, end="")
        print("  ]")   
    return tabla

def ganador(tabla, simbolo):
    c = len(tabla) - 1 
    cont3 = 0
    cont4 = 0
    for i in range(len(tabla)):
        cont = 0
        cont2 = 0
        #Filas y Columnas
        for j in range(len(tabla)):
            if tabla[i][j] == simbolo:
                cont += 1
            if tabla[j][i] == simbolo:
                cont2 += 1

        #Diagonal Principal
        if tabla[i][i] == simbolo:
            cont3 += 1

        #Diagonal Secundaria
        if tabla[i][c-i] == simbolo:
            cont4 += 1

        if cont == 3 or cont2 == 3 or cont3 == 3 or cont4 == 3:
            return True  

    return False    

def tablaLLena(tabla):
    for i in range(len(tabla)):
        for j in range(len(tabla)):
            if tabla[i][j] == " ":
                return False
    return False
        
def juego(tabla, posicion):
    p = int(input("Ingrese la posición: (1-9)"))
    tabla[p] = "x"
    

tabla = [["x","x","x"],
         ["x"," ","x"],
         ["x"," "," "]]

imprimir(tabla)
tabla[2][2] += "x"
print(ganador(tabla, "x"))
print(tablaLLena(tabla))