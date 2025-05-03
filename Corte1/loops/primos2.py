
a = 1

while a == 1:
    value = input('Ingrese un valor: ')
    value = int(value)

    
    for i in range(1, value + 1):
        conta = 0  # Contador de divisores

        for n in range(1, i + 1):
            if i % n == 0:
                conta += 1

        # Si tiene exactamente 2 divisores, es primo
        if conta == 2:
            print(f'{i} ES un primo\n')
        else:
            print(f'{i} NO es un primo\n')

    # Preguntamos si desea continuar
    a = int(input('¿Deseas continuar? Presiona 1 para hacerlo, otro número para salir: '))

print('Cerrando... ;)')