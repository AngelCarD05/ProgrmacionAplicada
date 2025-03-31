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


mi_NumList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
ordenar =  mi_NumList.sort()
print('Ordenando mi_NumList: ', ordenar)

#my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]
#print("Ordering my_NumList: ")
#my_NumList.sort()
#print(my_NumList)


