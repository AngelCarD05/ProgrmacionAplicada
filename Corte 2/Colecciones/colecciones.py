animales = {'gato', 'perro', 'pez_dorado', 'canario', 'gato'}
print(animales)

numeros_pares = {2, 4, 6, 8, 10}
numeros_grandes = {6, 7, 8, 9, 10}
print(end="\n")
print(numeros_grandes - numeros_pares)
print(numeros_grandes | numeros_pares)
print(numeros_grandes & numeros_pares)

print(end="\n")
print(animales)
print(sorted(animales))

print(end="\n")
print(list(range(10)))
print(list(range(1, 11)))
print(list(range(1, 11, 2)))

animales = ['gato', 'perro', 'pez_dorado', 'canario', 'gato']
conjunto_animales = set(animales)
lista_unica_animales = list(conjunto_animales)
tupla_unica_animales = tuple(lista_unica_animales)
print(end="\n")
print(conjunto_animales)
print(lista_unica_animales)
print(tupla_unica_animales)

canicas = {"roja": 34, "verde": 30, "marron": 31, "amarilla": 29}
colores = list(canicas)
cantidades = tuple(canicas.values())
conjunto_canicas = set(canicas.items())

print(end="\n")
print(colores)
print(cantidades)
print(conjunto_canicas)

diccionario = dict([(1, 2), (3, 4)])
print(end="\n")
print(diccionario)

cadena = "abracadabra"
print(len(cadena))
print(cadena.index("a"))
print(cadena[0])
print(cadena[3:5])

print("\n")
print('h' in 'abcd') 
print('ab' in 'abcd') 
print(['a', 'b'] in ['a', 'b', 'c', 'd'])

print("\n")
lista_abc = list("abracadabra")
print(lista_abc)

print("\n")
lista_l = ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']
cadena = "".join(lista_l)
print(cadena)

animales = ('gato', 'perro', 'pez')
print("\n")
print(" ".join(animales))
print(",".join(animales))
print(", ".join(animales))
print("gato    perro pez\n".split())
print("gato|perro|pez".split("|"))
print("gato, perro, pez".split(", "))
print("gato, perro, pez".split(", ", 2))

mi_tabla = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]
print("\n")
print(mi_tabla[0][0])
mi_tabla[0][0] = 42
print(mi_tabla)

mi_lista_2d = [
    [0],
    [1, 2, 3, 4],
    [5, 6],
]
print("\n")
print(mi_lista_2d)

mi_lista_3d = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
]
print("\n")
print(mi_lista_3d[0][0][0])
