from random import randint

def llnearSec(n):
    lista = []
    for i in range(1,n+1):
        lista += [i]
    return lista

def llenarAlea(n):
    lista = []
    num = randint(1,n)
    for i in range(1,n+1):
        while num in lista:
            num = randint(1,n)
        lista += [num]
    return lista
n = 10
i = 0
listaA = llnearSec(n)
listaB = llenarAlea(n)
for i in range(len(listaA)):
    print("La persona",listaA[i],"le dará el regalo a la persona",listaB[i])