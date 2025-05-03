# Obtener un valor usando su clave

alturas_edificios = {
    "Burj Khalifa": 828,
    "Torre de Shanghai": 632,
    "Abraj Al Bait": 601,
    "Ping An": 599,
    "Lotte World Tower": 554.5,
    "One World Trade": 541.3
}

print('Altura del Edificio Burj Khalifa', alturas_edificios["Burj Khalifa"]) 
print('Altura del Edificio Ping An', alturas_edificios["Ping An"])
# print(alturas_edificios["Landmark 81"])
# Clave no válida (no existe en el diccionario) Provoca un error

# Verificar si la clave existe:
clave_a_verificar = "Landmark 81"

if clave_a_verificar in alturas_edificios:
    print(alturas_edificios[clave_a_verificar])
else:
    print("La clave no existe en el diccionario.")

signos_zodiaco = {
    "agua": ["Cáncer", "Escorpio", "Piscis"],
    "fuego": ["Aries", "Leo", "Sagitario"],
    "tierra": ["Tauro", "Virgo", "Capricornio"],
    "aire": ["Géminis", "Libra", "Acuario"]
}

print(signos_zodiaco["tierra"])
print(signos_zodiaco["fuego"])

# Agregando una nueva clave y valor al diccionario
signos_zodiaco["energía"] = "No es un elemento del zodiaco"

if "energía" in signos_zodiaco:
    print('Energía:',signos_zodiaco["energía"])

# Para obtener el valor de agua Key se usa .get()
print(alturas_edificios.get("Torre de Shanghai"))
print(alturas_edificios.get("Mi Casa")) # Devuelve None



usuarios = {
    "TeraCoder": 100019,
    "PythonGuy": 182921,
    "SamLaJava": 123112,
    "LauraLoop": 102931,
    "KeithLlaves": 129384
}

# Obtener ID de un usuario específico
if usuarios.get("teraCoder") is None:
    id_tc = 1000
else:
    id_tc = usuarios.get("teraCoder")

print(id_tc)

if usuarios.get("superStackSmash") is None:
    id_stack = 100000

print(id_stack)


sorteo = {
    223842: "Osito de peluche",
    872921: "Boletas de concierto",
    320291: "Canasta de regalo",
    412123: "Collar",
    298787: "Fábrica de pasta"
}

# Eliminar una clave
print(sorteo.pop(320291, "Sin premio")) # Imprime lo que hay en la clave 320291 y elimina el elemento del diccionario
print(sorteo)
print(sorteo.pop(100000, "Sin premio")) 
print(sorteo)
print(sorteo.pop(872921, "Sin premio"))  
print(sorteo)


objetos_disponibles = {
    "poción de salud": 10,
    "pastel curativo": 5,
    "elixir verde": 20,
    "sándwich de fuerza": 25,
    "granos de estamina": 15,
    "estofado de poder": 30
}
# Eliminar y sumar valores a una variable
puntos_salud = 20
puntos_salud += objetos_disponibles.pop("granos de estamina", 0)
puntos_salud += objetos_disponibles.pop("estofado de poder", 0)
puntos_salud += objetos_disponibles.pop("pan místico", 0)

print(objetos_disponibles)
print(puntos_salud)

# Obtener todas las claves
notas_pruebas = {
    "Grace": [80, 72, 90],
    "Jeffrey": [88, 68, 81],
    "Sylvia": [80, 82, 84],
    "Pedro": [98, 96, 95],
    "Martín": [78, 80, 78],
    "Dina": [64, 60, 75]
}

print(list(notas_pruebas))

for estudiante in notas_pruebas.keys():
    print(estudiante)

# Obtener claves de diferentes diccionarios
usuarios = usuarios.keys()
ejercicios = {
    "funciones": 10,
    "sintaxis": 13,
    "flujo de control": 15,
    "bucles": 22,
    "listas": 19,
    "clases": 18,
    "diccionarios": 18
}.keys()

print(usuarios)
print(ejercicios)

# Obtener todos los valores
for lista_notas in notas_pruebas.values():
    print(lista_notas)

ejercicios = {
    "funciones": 10,
    "sintaxis": 13,
    "flujo de control": 15,
    "bucles": 22,
    "listas": 19,
    "clases": 18,
    "diccionarios": 18
}

# Obtener la suma de todos los valores
total = 0
for cantidad in ejercicios.values():
    total += cantidad
print(total)

# Obtener todos los elementos (clave, valor)
marcas_famosas = {
    "Apple": 184,
    "Google": 141.7,
    "Microsoft": 80,
    "Coca-Cola": 69.7,
    "Amazon": 64.8
}

# Obtener todos los elementos (clave, valor) y mostrarlos
for marca, valor in marcas_famosas.items():
    print(marca + " tiene un valor de " + str(valor) + " mil millones de dólares.")


porcentaje_mujeres = {
    "CEO": 28,
    "Gerente de Ingeniería": 9,
    "Farmacéutico": 58,
    "Médico": 40,
    "Abogado": 37,
    "Ingeniera Aeroespacial": 9
}
# Obtener el porcentaje de mujeres en cada ocupación
for ocupacion, porcentaje in porcentaje_mujeres.items():
    print("Las mujeres representan el " + str(porcentaje) + "% de " + ocupacion + "s.")