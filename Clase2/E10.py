num = 50
i = 0
r = "El numero " + str(num) + " es divisible para: "
for i in range(1,num//2+1,i+1):
    if num%i == 0:
    #     print(i, end=" ")#"end es para que imprima sin salto de linea
        r+= str(i)+", "
r += str(num)
print (r)
