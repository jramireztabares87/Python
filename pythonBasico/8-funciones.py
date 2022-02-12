#Ejemplo de funcion sencilla sin recibir parametros
"""
def imprimirMensaje ():
    print("Mensaje especial!")
    print("Mi primera funcion!")
    

imprimirMensaje()

"""
#Funcion con un retorno de valor, en este ejemplo la suma de dos numeros
def suma(a, b):
    print("La suma de dos numeros")
    suma = (a + b)
    return suma

sumatoria = suma(6,4)
print(sumatoria)
    

#Ejemplo de funcion sencilla recibiendo un parametro
"""
def conversacion(mensaje):    
    print("Hola como estas?" + "\n" + mensaje + "\nAdios!")
    
opcion = input("Elige una opción (1, 2, 3): ")

if opcion == "1":
    conversacion("Elegiste la opción " + opcion)
elif opcion == "2":
    conversacion("Elegiste la opción " + opcion)
else:
    conversacion("Elegiste la opción " + opcion)
"""    