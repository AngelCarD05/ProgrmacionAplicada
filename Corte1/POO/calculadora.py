class Calculadora:
    def _init_(self):
        pass

    def suma(self, num1, num2):
        return f'El resutlado de {num1} + {num2} es igual a {num1 + num2}'
    
    def resta(self, num1, num2):
        return f'El resutaldo de {num1} - {num2} es igual a {num1 - num2}'
    
    def multiplicacion(self, num1, num2):
        return f'El resultado de {num1} * {num2} es igual a {num1 * num2}'
    
    def division(self, num1, num2):
        if num2 != 0:
            return f'El resultado de {num1} / {num2} es igual a {num1/num2}'
        else:
            'No se puede dividir entre 0'
    
calculadora = Calculadora()

while True:
    print('----------CALCULADORA----------')
    print('1. Suma')
    print('2. Resta')
    print('3. Multipliación')
    print('4. División')
    print('5. Salir')
    print('-------------------------------')
    opcion = int(input('Elige una Opción: '))
    print('-------------------------------')
    num1 = int(input('Ingresa el Número 1: '))
    num2 = int(input('Ingresa el Número 2: '))
    print('-------------------------------')

    if opcion == 5:
        print('Saliendo de la Calcaladora...')
        break
    elif opcion == 1:
        print(calculadora.suma(num1, num2))
    elif opcion == 2:
        print(calculadora.resta(num1, num2))
    elif opcion == 3:
        print(calculadora.multiplicacion(num1, num2))
    elif opcion == 4:
        print(calculadora.division(num1, num2))
    else:
        print('Opción no Válida')