import random
import csv
import time

archivo_csv = 'random.csv'

with open(archivo_csv, mode='w', newline='') as archivo:
    writer = csv.writer(archivo)

    while True:
        # Generar un número aleatorio entre 0 y 1
        numero_aleatorio = random.random()
        if numero_aleatorio == 0.0:
            continue
        
        writer.writerow([numero_aleatorio]) # Escribir el número en el archivo CSV
        print(numero_aleatorio) 
        time.sleep(1)