k = 150
listaP = [80,34,80,23,70]
mayorP = 0
for i in range(len(listaP)):
    for j in range(i+1,len(listaP)):
        peso = listaP[i] + listaP[j]
        if peso <= k:
            print("Peso de ",listaP[i],"kg + ",listaP[j],"kg = ",peso,"kg")
            if mayorP < peso:
                mayorP = peso
print ("El peso mas grande encontrado es de:",mayorP,"kg")