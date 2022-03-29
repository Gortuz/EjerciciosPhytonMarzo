entrada = int(input("Ingrese el numeo de dias: "))

anios = entrada//365
meses = (entrada%365)//30
dias = (entrada%365)%30

print("Usted tiene",anios,"años/s",meses,"mes/es",dias,"dias/s de vida")