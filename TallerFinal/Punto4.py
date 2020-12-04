n= int(input("Escriba el número de nuggets de pollo que desea\n"))
def comprar(n):
    a = 6
    b = 9
    c = 20
    d = a+b
    x = n//a
    y = n//b
    z = n//(a+b)
    w = n//c

    if n%a == 0:
        if n%b == 0:
            print("Puede comprar ",x, " bolsas de", a, " nuggets de pollo")
            print(" tambien puede comprar ",y, " bolsas de ", b, " nuggets de pollo")
        elif n%c == 0:
        	print("Puede comprar ",x, " bolsas de", a, " nuggets de pollo")
        	print(" tambien puede comprar ", w, " bolsas de ",c," nuggets de pollo")
        elif n%b==0 and n%c==0:
            print("Puede comprar bolsas de a 6, de a 9 y de a 20 nuggets de pollo")
        else:
            print("Puede comprar ", n//a, " bolsas de ", a, " pollos")

    elif n%d==0:
            print("Puede comprar " ,z, " bolsas de ", a, " y ", z, "bolsas de", b )

    elif n%c == 0:
    	print("Puede comprar ", n//c, " bolsas de ", c, " nuggets de pollo")

    elif n%b == 6:
    	print("Puede comprar ", 1, " bolsa de ", a ," nuggets de pollo y ", (n-(n%9))//9, " bolsas de nuggets de pollo de ", b)

    elif n%b == 0:
    	print("Puede comprar ", n//9, " boslas de ", b, " pollos ")

    else:
        print("No se puede comprar esta cantidad")

print(comprar(n))