def bisiestosEntre(anioIni,anioFin):
    aux = 0
    if(anioIni > anioFin):
        aux = anioIni
        anioIni = anioFin
        anioFin = aux

    i = 0
    for i in range(anioIni,anioFin+1,i+1):
        if((i%4 == 0) and (i%400 == 0 or  i%100!=0)):
            print(i,end="  ")
    return 0

anioIni = int(input("Año menor: "))
anioFin = int(input("Año mayor: "))
bisiestosEntre(anioIni,anioFin)
