while True:
    valor = int(input("Digite un número entero positivo: "))

    if valor >= 0:
        factorial = 1
        for i in range(1, valor + 1):
            factorial *= i
        print(f"El resultado de {valor}! es: {factorial}")
    else:
        print("Valor inválido. Inténtalo de nuevo.")
