
num1 = int(input("Ingresa el primer número del rango: "))
num2 = int(input("Ingresa el segundo número del rango: "))
print("Los números divisibles entre 12 en el rango son:")
for i in range (num1, num2+1):
    if i % 12 == 0:
        print(i)