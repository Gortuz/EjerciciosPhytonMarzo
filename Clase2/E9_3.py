hora = 17
min = 59
seg = 58

print("Hora actual: "+str(hora)+":"+str(min)+":"+str(seg))
if(hora <= 23 and hora >= 0) and (min <= 60 and min >= 0) and (seg <= 60 and seg >=0):
    seg += 1
    if seg == 60:
        seg = 0
        min += 1
    if min == 60:
        min = 0
        hora += 1
    if hora == 24: 
        hora = 0
    print("La hora un segundo despues: "+str(hora)+":"+str(min)+":"+str(seg))
else:
    print("Ingrese una hora correcta")