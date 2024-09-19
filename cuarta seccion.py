#cuarta seccion Tipos de datos de Python
"""
Tipos de datos integrados
En programación, el tipo de datos es un concepto importante.

Las variables pueden almacenar datos de diferentes tipos, y diferentes tipos pueden hacer cosas diferentes.

Python tiene los siguientes tipos de datos integrados de forma predeterminada, en estas categorías:

Tipo de texto: str
Tipos numéricos: int, float, complex
Tipos de secuencia: list, tuple, range
Tipo de mapeo: dict
Tipos de conjuntos: set,frozenset
Tipo booleano: bool
Tipos binarios: bytes, bytearray, memoryview
Ninguno Tipo: NoneType
"""
x = str("Hello World") #str
x = int(20) #int
x = float(20.5) #float
x = complex(1j) #complex para poner numeros y letras

x = list(("apple", "banana", "cherry")) #list Las listas se utilizan para almacenar varios elementos en una sola variable.

thistuple = ("apple", "banana", "cherry") #Las tuplas se utilizan para almacenar varios elementos en una sola variable.
print(thistuple)#pero no se puede modificar luego de ser creada y se debe defiir el tamano el cual no se puede modificar

"""
La range()función devuelve una secuencia de números, comenzando desde 0 de
forma predeterminada, y se incrementa en 1 (de forma predeterminada) y se detiene antes de un número especificado.

Sintaxis
range(start, stop, step)
"""
x = range(6)
for n in x:
  print(n)

"""
Dict
Los diccionarios se utilizan para almacenar valores de datos en pares clave:valor.

Un diccionario es una colección ordenada*, modificable y que no permite duplicados.
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

x = set(("Lyn", "Alexa", "Juli")) #no se pueden poner duplicados

x = frozenset(("apple", "banana", "cherry")) #frozenset este es inmutable no se puede modoficar depues de crearlo

x = bool(5) #bool si una expresión es Trueo False.
"""
La bytes()función devuelve un objeto de bytes.

Puede convertir objetos en objetos de bytes o crear objetos de bytes vacíos del tamaño especificado.

La diferencia entre bytes()y bytearray()es que bytes()devuelve
un objeto que no se puede modificar y bytearray()devuelve un objeto que se puede modificar.
"""
x = bytes(5) #bytes 

"""
La bytearray()función devuelve un objeto bytearray.

Puede convertir objetos en objetos bytearray o crear objetos bytearray vacíos del tamaño especificado.
Sintaxis
bytearray(x, encoding, error)
"""
x = bytearray(5) #bytearray

 x = memoryview(bytes(5)) #memoryview Crear e imprimir un objeto de vista de memoria:

x = memoryview(b"Hello")

print(x)

#return the Unicode of the first character
print(x[0])

#return the Unicode of the second character
print(x[1])

