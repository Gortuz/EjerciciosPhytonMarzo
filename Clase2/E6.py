sexo = "f"
edad = 59
cotizaciones = 800
aniosServicio = 26

#Para hacwer 
if (aniosServicio >= 25 and cotizaciones >= 750) and ((sexo == "m" and edad >= 60) or (sexo == "f" and edad >= 55)): 
        print("Usted aplica para ser jubilado")
else:
    print("Usted NO aplica para ser jubilado")
