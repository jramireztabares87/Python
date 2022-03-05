# Los sets o conjuntos son una colección desordenada de elementos únicos e inmutables.
# A continuación, una serie de ejemplos en donde cada salida se da de forma ordenanda:
from pprint import pprint


my_set ={3, 4, 5}
print("my_set =", my_set)
#output my_set = {3, 4, 5}

my_set2 ={"Hola", 23.3, False, True}
print("my_set2 =", my_set2)
#output my_set2 = {False, True, 'Hola', 23.3}

my_set3 ={3, 3, 2}
print("my_set3 =", my_set3)
#output my_set3 = {2, 3}

# Para este caso la salida es un error de tipo TypeError: unhashable type: 'list' ya que un set no
# puede almacenar una lista, dado que estas son mutables y el set es inmutable

# my_set4 ={[1,2,3],4}
# print("my_set4 =", my_set4)

# Traceback (most recent call last):
#   File "D:\JohanRamirezTabares\Documentos\Platzi\python\3-pythonProfesional\11-set.py", line 12, in <module>
#     my_set4 ={[1,2,3],4}
# TypeError: unhashable type: 'list'

#-----COMO CREAR UN SET VACIO-----------------------------------------------------------------------------

# A pesar de que un set se encuentra dentro de conchetes, no se puede inicializar con estos, puesto que también corresponden a un diccionario
empty_set = {}
print(type(empty_set))
# output <class 'dict'>


# Para declarar de forma correcta un set, se debe usar la clausula set seguido de paréntesis ()
empty_set = set()
print(type(empty_set))
# output <class 'set'>


#-----COMO CONVERTIR LISTAS Y TUPLAS EN SETS----------------------------------------------------------------
my_list = [1,1,2,3,4,4,5]
my_set = set(my_list)
pprint(my_set)
#Al objeto my_list ser convertido en un set, se eliminan los elementos repetidos y estos se ordenan
# output {1, 2, 3, 4, 5}

my_tuple = ("Hola", "Hola","Hola", 1)
my_set2 = set(my_tuple)
print(my_set2)
#Al objeto my_tuple ser convertido en un set, se eliminan los elementos repetidos y estos se ordenan
# output {1, 'Hola'}


#-----ADICIONAR ELEMENTOS A UN SET----------------------------------------------------------------
my_set = {1, 2, 3}
print(my_set)

# Añadir un elemento
my_set.add(4)
print(my_set)

# Añadir múltiples elemntos
my_set.update([1,2,5])
print(my_set)

# Añadir multiples elementos
my_set.update((1, 7, 2), {6, 8})
print(my_set)

#-----BORRAR ELEMENTOS DE UN SET----------------------------------------------------------------
my_set = {1, 2, 3, 4, 5, 6, 7}
print(my_set)

# Borrar un elemento existente con discard
my_set.discard(1)
print(my_set)

# Borrar un elemento existente con remove
my_set.remove(2)
print(my_set)

# Borrar un elemento inexistente con discard
# Con este opcion se eleva un error de tipo KeyError
# my_set.discard(10)
# print(my_set)

# Borrar un elemento inexistente con remove
# Con este opcion se eleva un error de tipo KeyError
# my_set.remove(12)
# print(my_set)

# Borrar un elemento aleatorio
my_set.pop()
print(my_set)

# Limpiar el set
my_set.clear()
print(my_set)