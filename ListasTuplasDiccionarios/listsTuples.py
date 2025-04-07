#Listas

mi_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']

print(mi_lista) #Imprime Toda la Lista
print(type(mi_lista))
print(mi_lista[2]) #Imprime lo que hay en la posición 2

print('Tamaño de mi_lista: ', len(mi_lista)) #Imprime el tamaño de una lista
print(mi_lista[0:2]) #Imprime una lista con los dos primeros elementos de la lista
print(mi_lista[:2]) #Imprime una lista con los dos primeros elementos de la lista

mi_lista.append('Blanco') #Agrega un elementos al final de la lista
print(mi_lista)

mi_lista.insert(3, 'Negro') #Agrega un elemnto despues de la posicion 3
print(mi_lista)

mi_lista.extend(['Marron', 'Gris']) #Concatena otra lista
print(mi_lista)

print(mi_lista.index('Azul')) #Imprime la posición en el que esta el elemento 'Azul'

mi_lista.remove('Marron') #Elimina el elemento de la lista
print(mi_lista)

mi_lista.insert(8, 'Marron') #Inserta un elemento en la posición deseada
print(mi_lista)

print(mi_lista.pop()) #Elimina el ultimo elemento de la lista e imprime el elemnto eliminado


tamaño = len(mi_lista) #Permite conocer el tamaño de la lista
print('Tamaño = ', tamaño)

mi_lista_3 = mi_lista*3 
print('mi_lista_3: ', mi_lista_3) #Imprime cada elemnto de mi_lista 3 veces

mi_listaSort = mi_lista.sort() #Ordena los elementos de menor a mayot por defecto. Sin embargo, al imprimir nos indida Sorte: None porque la lista no esta comprendida por números.
print('Sort: ', mi_listaSort)


my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]
print("Ordenado mi_NumList: ")
my_NumList.sort() #Ordena los elementos de menor a mayor
print(my_NumList)

my_NumList.sort(reverse=True) #Ordena los elementos de mayor a menor
print('De menor a mayor: ', my_NumList)


#Tuplas

print('################Tuplas#################')

mi_tupla = tuple(mi_lista) #Convierte una lista en una tupla
print('mi_tupla:', mi_tupla)
print(type(mi_tupla)) #Imprime el tipo de dato de mi_tupla

print(mi_tupla[0]) #Imprime el primer elemento de la tupla
print(mi_tupla[2]) #Imprime el tercer elemento de la tupla

print('Rojo' in mi_tupla) #Verifica si el elemento Rojo esta en la tupla devoliviendo True o False
print(mi_tupla.count("Rojo")) #Cuenta cuantas veces aparece el elemento Rojo en la tupla

mi_tupla_unitaria = ('Blanco') #Tupla con un solo elemento
print(mi_tupla_unitaria)

mi_tupla = 'Gaspar', 5, 8, 1999 #Empaquetado de tuplas, tupla sin parentesis
print(mi_tupla)

nombre, dia, mes, año = mi_tupla #Desempaquetado de tuplas, asignando cada elemento a una variable con el mismo orden
print('Nombre:', nombre)
print('Dia:', dia)
print('Mes:', mes)
print('Año:', año)

mi_lista2 = list(mi_tupla) #Convierte una tupla en una lista
print('mi_lista2:', mi_lista2)
print(type(mi_lista2)) #Imprime el tipo de dato de mi_lista2