a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))


print("La ecuacion es: "+str(a)+"x + "+str(b)+" = 0")

if a == 0 == b:
    r = "Todos los números son solucion"
elif a == 0:
    r = "No exsiste solución"
else:
    r = "La única solución es: "+str(-b/a)

print(r)