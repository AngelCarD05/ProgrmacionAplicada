class Perro:
    def __init__(self, nombre, edad):
        
        self.nombre = nombre
        self.edad = edad

    def descripcion(self):
        return f"{self.nombre} tiene {self.edad} años de edad"
    
    def ladrar(self, sound):
        return f'{self.nombre}: dice {sound}'

perro = Perro('Snoopy', 2) 
print(perro.descripcion())
print(perro.ladrar('Guau, Guau, Guau'))