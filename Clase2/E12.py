def piramide(niveles):
    i = 0
    for i in range(1,niveles+1,i+1):
        for e in range(niveles-i):
            print("  ",end="")
        for a in range((2*i-1)):
            print(" *",end="")
    print()

niveles = int(input("Ingrese el número de niveles de la figura: "))
piramide(niveles)
