
print("Adivinador de numero")
y=input("ingrese un numero entre 0 y 1024: ")
x= int(y)
a = 0
b = 1024
test = True

if x== 0:
    print("su numero es 0, gracias por jugar")
    test=False
else :
    if x==1024:
        print("su numero es 1024, gracias por jugar")
        test=False
    while test == True:
        n = int((a+b)/2) # (0+ 1024) /2 = 512
        if n == x:
            print("su numero es ", n, ", gracias por jugar")
            break
        else:
            if n < x:
                a=n
            else:
                b=n
