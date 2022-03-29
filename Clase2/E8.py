jornada = 48
horasTrabajadas = int(input("Ingrese sus horas trabajadas: "))
pagoHora = 2;
pagoExtra = 3.5

if horasTrabajadas <= jornada:
    salario = horasTrabajadas * pagoHora
else:
    salario = (jornada * pagoHora) + ((horasTrabajadas - jornada) * pagoExtra)

print ("Su pago total es de: $",salario)

