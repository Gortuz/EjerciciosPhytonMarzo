aciertos = int(input("Ingrese el numero de aciertos: "))
errores = int(input("Ingrese el numero de errores: "))
total = aciertos + errores

pCorrecto = (100/total) * aciertos
pErrores = (100/total) * errores

print("Su puntaje final fue: ",aciertos,"/",errores)
print("Porcentajes:\nAciertos: %.2f"%pCorrecto,"\nErrores: %.2f"%pErrores)
