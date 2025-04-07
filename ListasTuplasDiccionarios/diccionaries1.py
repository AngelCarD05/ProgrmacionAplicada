# Diccionarios

sensores = { 
    'Sala de Estar:': 21,
    'Cocina:': 23,
    'Dormitorio:': 20,
    'Despensa:': 22,
}

num_camaras = {
    'Jardín Trasero:': 6,
    'Garaje:': 2,
    'Camino de Entrada:': 1,
}

print('Sensores: ', sensores) #Imprime el diccionario 'Sensores'
print('Número de Cámaras: ', num_camaras) #Imprime el diccionario 'Número de Cámaras'

traducciones = {
    'Mountain': 'Montaña',
    'Bread' : 'Pan',
    'Friend': 'Amigo',
    'Mellon': 'Melón',
    'Horse': 'Caballo',
}

print('Traducciones: ', traducciones) #Imprime el diccionario 'Traducciones'

# Para las claves de un diccionario deben ser inmbutables (int, str, float, tuplas). Por lo tanto, no se pueden usar listas como claves de un diccionario.
#potencias = {
#    (1, 2, 4, 8, 16) : 2,
#    (1, 3, 9, 27, 81) : 3
#}

#print('Potencias: ', potencias)

# Teniendo en cuenta lo anterior se podría hacer lo siguiente:
niños = {
    'von Trapp': [
        'Johannes',
        'Rosmarie',
        'Eleonore',
    ],

    'Coleone': [
        'Sonny',
        'Fredo',
        'Michael'
    ]
}
print('Niños:', niños)

mi_diccionario_vacio = {} #Crea un diccionario vacío
print('Diccionario vacío: ', mi_diccionario_vacio) 


menu = {
    'Avena': 3,
    'Tostadas': 6,
    'Jugo de Zanahoria': 5,
    'Muffin de Arándano': 2,
}
print('Antes: ', menu)

menu['Cheesecake'] = 4 #Agrega un elemento al final del diccionario
print('Después: ', menu)


animales_en_el_zoologico = {'Dinosaurios:': 0}
animales_en_el_zoologico = {'Caballos': 2} # Reemplaza la clave 'Dinosaurios' por 'Caballos' y su valor por 2
print('Animales en el zoológico: ', animales_en_el_zoologico)


# Agregar o Actualizar un elemento en el diccionario
print('Antes:', sensores)

sensores.update({
    'Sala de Huéspedes:': 25,
    'Patio:': 34,
})
print('Después:', sensores)

id_usuarios = {
    'TeraCode': 901829,
    'ProProgrammer': 119238,
}
print('ID de usuarios: ', id_usuarios)

id_usuarios.update({
    'TheLooper': 138475,
    'StringQueen': 85739,
})
print('ID de usuarios actualizado: ', id_usuarios)

# Sobreescribir un elemento en el diccionario
print('Antes:', menu)
menu['Avena'] = 4 #Sobreescribe el valor de la clave 'Avena' por 4
print('Después:', menu)


ganadores_oscar = {
    'Mejor Imágen': 'La La Land',
    'Mejor Actor': 'Casey Affleck',
    'Mejor Actriz': 'Emma Stone',
    'Característica Animada': 'Zootopia',
}
print('Antes:', ganadores_oscar)

ganadores_oscar.update({
    'Actores de Apoyo': 'Viola Davis',
})
print('Después1:', ganadores_oscar)

ganadores_oscar['Mejor Imágen'] = 'Moonlight' #Sobreescribe el valor de la clave 'Mejor Imágen' por 'Moonlight'
print('Después2:', ganadores_oscar)

# Unir Dos Listas
nombres = ['Jeeny', 'Alexus', 'Sam', 'Grace']
alturas = [61, 70, 67, 64]

zipEstudiantes = zip(nombres, alturas) #Une dos listas en una sola lista de tuplas
print('Zip Estudiantes: ', zipEstudiantes) 

estudiantes = { key: value for key, value in zipEstudiantes} #Convierte la lista de tuplas en un diccionario
print('Estudiantes: ', estudiantes) #Imprime el diccionario 'Estudiantes'


bebidas = {'Espresso', 'Chai', 'Decaf', 'Drip'}
cafeina = {64, 40, 0, 120}

zip_bebidas = zip(bebidas, cafeina) #Empaqueta dos listas
print('Zip Bebidas: ', zip_bebidas) 

bebidas_cafeina = {key:value for key, value in zip_bebidas} #Convierte la lista de tuplas en un diccionario
print('Bebidas Cafeina: ', bebidas_cafeina) 


canciones = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
num_reproducciones = [78, 29, 44, 21, 89, 5]

reproducciones = {key:value for key, value in zip(canciones, num_reproducciones)} #Convierte la lista de tuplas en un diccionario
print('Reproducciones: ', reproducciones)

reproducciones.update({
    'Purple Haze': 1, # Agrega un elemento al final del diccionario
    'Respect': 2, # Sobreescribe el valor de la clave 'Respect' por 2
})

print('Reproducciones actualizado: ', reproducciones)

# Se puede colocar como valor un diccionario vacío o un diccionario con valores
libreria = {"The Best Songs": reproducciones, "Sunday Feelings": {}}
print(libreria)