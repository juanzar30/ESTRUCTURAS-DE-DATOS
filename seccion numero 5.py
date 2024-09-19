# quinta seccion Numeros
"""
Hay tres tipos numéricos en Python:

int
float
complex
"""
"""
Las variables de tipo numérico se crean cuando se les asigna un valor:
"""
a = 1    # int
b = 2.8  # float
c = 30j   # complex

"""
Para verificar el tipo de cualquier objeto en Python, utilice la type()función:
"""
print(type(a))
print(type(b))
print(type(c))

"""
Int
Int, o entero, es un número entero, positivo o negativo, sin decimales, de longitud ilimitada.
"""
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

"""
float
Un número flotante o "número de punto flotante" es un número, positivo o negativo, que contiene uno o más decimales.
"""
a = 1.10
b = 1.0
c = -35.59

print(type(a))
print(type(b))
print(type(c))

"""
Complejo
Los números complejos se escriben con una "j" como parte imaginaria:
"""
a = 3+5j
b = 5j
c = -5j

print(type(a))
print(type(b))
print(type(c))

"""
Conversión de tipos
Puede convertir de un tipo a otro con los métodos int(), float()y complex():
"""
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convertir de int to float:
a = float(x)

#convertir de float to int:
b = int(y)

#convertir de int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

"""
Número aleatorio
Python no tiene una random()función para crear un número aleatorio, pero Python
tiene un módulo incorporado llamado randomque se puede usar para crear números aleatorios:
"""
import random

print(random.randrange(1, 100))