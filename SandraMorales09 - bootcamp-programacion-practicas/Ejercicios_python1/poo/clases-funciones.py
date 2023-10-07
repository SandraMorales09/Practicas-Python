# Clases
# fundamentos de programación orientada a objetos

"""
Existen cuatro tipos de notación

Camel Case -> contarElementos

Pascal Case -> ContarElementos

Snake Case -> contar_elementos

Kebab Case -> contar-elementos

"""
edad1 = 27
class Persona :
    # Primero los atributos de la clase

    # Constructor
    def __init__(self, nombre, edad, altura) :
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def leer_edad(self) :
        return self.nombre + " tiene " + str(self.edad) + " años"

jesus = Persona("Jesús", 27, 1.75)
print(jesus.leer_edad())
print(jesus.altura)

mari = Persona("Mari", 25, 1.60)
print(mari.leer_edad())
print(mari.altura)

print("--------------------------------------")

#  ---------------- OTRA FUNCIÓN -------------------

class Perro :
    tipo = "canino" # Variable va a ser compartida con TODAS LAS INSTANCIAS
    #trucos = [] # Variable va a ser compartida con TODAS LAS INSTANCIAS

    def __init__(self, nombre) :
        self.nombre = nombre
        self.trucos = []

    def aprender_truco(self, truco) :
        self.trucos.append(truco)

puppy = Perro("Puppy")
puppy.aprender_truco("Dar la patita")

manchas = Perro("Manchas")
manchas.aprender_truco("Hacerse el muertito")

print(puppy.tipo)
print(manchas.tipo)

print(puppy.nombre)
print(manchas.nombre)

print(puppy.trucos)
print(manchas.trucos)