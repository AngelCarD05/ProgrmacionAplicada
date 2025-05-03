a =  int(input("Ingrese el número a: "))
b = float(input("Ingrese el número b: "))
c = a + b

if a == b:
    print("Los números son iguales")
else:
    print("Los números son diferentes")

print("El tipo de dato de a es:", type(a))
print("El tipo de dato de b es:", type(b))
print("c =", c)

if type(a) is type(b):  
    print("Los tipos de datos  de a y b son iguales")
else:
    print("Los tipos de datos de a y b son diferentes")