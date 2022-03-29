frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
cont = 0
for i in frase:
    if(i == letra):
        cont += 1

if cont != 0:
    print("La letra '"+letra+"' se repite "+str(cont)+" veces en la frase")
else:
    print("La letra '"+letra+"' no se encontro en la frase")
