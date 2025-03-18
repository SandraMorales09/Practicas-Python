# Conjuntos o sets
"""
NO ORDENADA Y SIN ELEMENTOS REPETIDOS

Operaciones logicas como: unión, intersección, diferencia...
"""

frutas = {'sandia', 'kiwi', 'pera', 'sandia', 'melon', 'uva'}
print(frutas)

palabra1 = set("abracadabra")
print(palabra1)

lista_frutas = ['sandia', 'kiwi', 'mango', 'sandia', 'melon', 'uva']
lista_frutas = list( set(lista_frutas) )
lista_frutas.sort()
print(lista_frutas)

print('kiwi' in frutas)
print('fresa' in frutas)

palabra1 = set( 'Ābù lā kǎ dá bù lā' )
palabra2 = set('abracadabra')

print(palabra1)
print(palabra2)

# Diferencia con conjuntos
print(palabra1 - palabra2) # Todas las letras que estén en palabra1 pero no en palabra2
print(palabra2 - palabra1)

# Union 
print(palabra1 | palabra2) # todas las letras que estén en palabra1 y palabra2 o ambas. Sin repetirse

# Intersección 
print(palabra1 & palabra2) # Todas las letras que estén en AMBOS conjuntos

# Diferencia simetrica
print(palabra1 ^ palabra2) # todas las letras qeu estén en palabra1 y en palabra2 pero no en ambas

# Comprensión de conjuntos
a = { elemento for elemento in "abracadabra" if elemento not in "abc"}
print(a)