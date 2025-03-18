# Una cola se basa en el principio de el primero que llega es el primero que sale
# FIFO - First In First Out

# Esto es una estructura de datos en Python que implementa una cola
from collections import deque

alumnos = deque(["victor", 'michael', 'leo', 'asrael'])
print(alumnos)

alumnos.append("Krisprkas")
alumnos.append("joshua")

print(alumnos)

alumnos.popleft()
print(alumnos)

alumnos.popleft()
print(alumnos)

print("-----------------------------------------------")

cola1 = []

cola1.append("Conejo")
cola1.append("Chunmal")
cola1.append("Manchas")

print(cola1)

cola1.pop(0)
print(cola1)

cola1.pop(0)
print(cola1)