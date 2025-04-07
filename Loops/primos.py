import time


tiempo_inicio = time.time() # Guaradar el tiempo de inicio


for numero in range(0, 31):
    divisores = 0

    # Contar los divisores del número
    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            divisores += 1

    # Si el número tiene exactamente dos divisores, es primo
    if divisores == 2:
        print(f"{numero} es un número primo")
    # Si el número tiene más de dos divisores, no es primo    
    else:
        print(f"{numero} no es un número primo")

tiempo_fin = time.time()

print("Tiempo de ejecución:", (tiempo_fin - tiempo_inicio) * 1000, "ms")



