"""
Archivos JSON

asociativos 
conjunto de pares clave:valor

"""
contactos = {
    'clave': 'VALOR',
    'nombre': 'Sandra',
    'apellidos': 'Roxana',
    'telefono': '4488632956',
    'edad': 27,
    'idiomas': ['español', 'íngles', 'japones', 'albures'],
    'vivo': True,
    'nombre': 'Sandra'
}

print(contactos['nombre'])
print(contactos['idiomas'])
del contactos['clave']
print(contactos)
contactos['correo'] = 'sadiashadow@gmail.com'
print(contactos)
contactos['nombre'] = 'Leo'
print(contactos)

print(list(contactos))
print(sorted(contactos))

print(contactos)

print('Leo' in contactos)
print('telefono' in contactos)

print("----------------------------------------------------")

telefonos = {
    "fabricante": "Xiaomi",
    "precio": 6499,
    "versiones": {
        "nombre": "Xiaomi 12 pro + 5G"
        }

}

celulares = dict([
    ('camara', "50 MP"),
    ('batería en mAh', 5000),
    ('camara', "70 MP"),
    ('pantalla', "OLED"),
    ('pantalla', "OLED21324423423")
])

print(celulares)

celulares = dict(
    camara = "50MP",
    bateria = 5000,
    pantalla = "OLED"
)

print(celulares)

# Comprensión de diccionarios
mi_diccionario = { numero: numero**2 for numero in (2, 3, 4, 5) }
print(mi_diccionario)

# Iteraciones sobre los diccionarios
pokemones = {
    'charmander': 'fuego',
    'metagross': 'acero',
    'tapu koko': 'electrico'
}

print("---------------------------------------------")
"""
tipo, tipo_secundario, pokemon, _, _ = ("agua", "tierra", "swampert", 'alegre', 'brujerias')
print(tipo)
"""

print("---------------------------------------------")

print(pokemones.items())

for nombre, tipo in pokemones.items() :
    print(nombre, tipo)


pokemones_datos = pokemones.items()


# Enumarate que nos devuelve un objeto enumerador
print(list(enumerate(['conejo', 'tigre', 'pez koi', 'perro'])))

for i, v in enumerate(['conejo', 'tigre', 'pez koi', 'perro']) :
    print(i, v)

# ZIP Itera sobre varios iterables en paralelo y genera tuplas

pregunta = ['telefono', 'nombre', 'comida favorita']
repuestas = ['4488632956', 'Sandra']

asociacion = zip(pregunta, repuestas)
print(asociacion)

for p, r in asociacion :
    print(p, r)


# FUNCIONES DE LOS DICCIONARIOS

# Función keys()
# Obtienes todas las claves del diccionario
print(pokemones.keys())

# Función values()
# Obtiene todos los valores del diccionario
print(pokemones.values())

# Función items()
# Devuelve todas las claves y los valores
print(pokemones.items())

