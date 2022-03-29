

def imprimir(dic):
    for i in dic:
        print("Codigo:",i," - Nombre",dic[i])

def agregarEstudiante(dic,codigo,nombre):
    dic[codigo] =[]
    dic[codigo].append(nombre)
    dic[codigo].append([])
     
def agregarNotas(dic, codigo,nota):
    dic[codigo][1] += [nota]

def promedio(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma/len(lista)

dic = {}
imprimir(dic)
agregarEstudiante(dic,"001","Kevin")
agregarNotas(dic,"001",10)
agregarNotas(dic,"001",8)
imprimir(dic)
print(promedio(dic["001"][1]))


