n = int(input("Ingrese el número máximo: "))
for i in range(1,n+1):
    if i%5 == 0 and i%3 == 0:
        print(i," FizzBuzz")
    elif i%3 == 0:
        print(i," Fizz")
    elif i%5 == 0:
        print(i," Buzz")
    


        